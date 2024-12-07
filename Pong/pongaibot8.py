import math

# Global variables to track ball state
previous_ball_position = [0, 0]
previous_paddle_position = 0
paddle_speed = 1

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """
    Improved Pong AI with enhanced ball prediction, efficient movement, and strategic targeting.
    """
    global previous_ball_position, previous_paddle_position, paddle_speed

    # Get ball, paddle, and table dimensions
    ball_center = [
        ball_frect.pos[0] + ball_frect.size[0] / 2,
        ball_frect.pos[1] + ball_frect.size[1] / 2,
    ]
    paddle_center = [
        paddle_frect.pos[0] + paddle_frect.size[0] / 2,
        paddle_frect.pos[1] + paddle_frect.size[1] / 2,
    ]
    table_height = table_size[1]

    # Determine if the paddle is on the left or right side
    is_left_paddle = paddle_center[0] < table_size[0] / 2

    # Ball velocity
    ball_velocity = [
        ball_center[0] - previous_ball_position[0],
        ball_center[1] - previous_ball_position[1],
    ]
    previous_ball_position = ball_center

    # Paddle speed
    if abs(paddle_center[1] - previous_paddle_position) > 0:
        paddle_speed = abs(paddle_center[1] - previous_paddle_position)
    previous_paddle_position = paddle_center[1]

    # Return to the middle if the ball is moving away
    if (is_left_paddle and ball_velocity[0] > 0) or (not is_left_paddle and ball_velocity[0] < 0):
        if paddle_center[1] < table_height / 2:
            return "down"
        elif paddle_center[1] > table_height / 2:
            return "up"
        else:
            return None

    # Predict the ball's y-coordinate at the paddle's x-plane
    def predict_ball_y(ball_center, ball_velocity, paddle_x, table_height):
        if ball_velocity[0] == 0:
            return ball_center[1]

        # Time to reach the paddle's x-plane
        time_to_paddle = (paddle_x - ball_center[0]) / ball_velocity[0]
        predicted_y = ball_center[1] + ball_velocity[1] * time_to_paddle

        # Handle wall bounces
        while predicted_y < 0 or predicted_y > table_height:
            if predicted_y < 0:
                predicted_y = -predicted_y
            elif predicted_y > table_height:
                predicted_y = 2 * table_height - predicted_y

        return predicted_y

    predicted_y = predict_ball_y(
        ball_center, ball_velocity, paddle_frect.pos[0], table_height
    )

    # Target opponent's weak spot
    opponent_center = other_paddle_frect.pos[1] + other_paddle_frect.size[1] / 2
    if opponent_center > table_height / 2:
        target_y = table_height / 4  # Target top quarter
    else:
        target_y = 3 * table_height / 4  # Target bottom quarter

    # Adjust the predicted y to direct the ball to the target
    def adjust_hit_position(predicted_y, paddle_center_y, paddle_size, target_y):
        if abs(target_y - predicted_y) < paddle_size / 2:
            return target_y
        return predicted_y

    adjusted_y = adjust_hit_position(
        predicted_y, paddle_center[1], paddle_frect.size[1], target_y
    )

    # Move paddle to align with the adjusted hit position
    if paddle_center[1] < adjusted_y:
        return "down"
    elif paddle_center[1] > adjusted_y:
        return "up"
    else:
        return None
