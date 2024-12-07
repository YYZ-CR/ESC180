# Global variables to track ball state
previous_ball_position = None
ball_last_hit_by_ai = False

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """
    Enhanced AI logic for the Pong game that prioritizes hitting the ball with a paddle corner.
    - paddle_frect: The AI's paddle rectangle (fRect object).
    - other_paddle_frect: The opponent's paddle rectangle (fRect object).
    - ball_frect: The ball's rectangle (fRect object).
    - table_size: Dimensions of the table (width, height).
    """
    global previous_ball_position, ball_last_hit_by_ai

    # Paddle parameters
    paddle_x = paddle_frect.pos[0]  # X-coordinate of the paddle's vertical plane
    paddle_top_edge = paddle_frect.pos[1]  # Top edge of the paddle
    paddle_bottom_edge = paddle_frect.pos[1] + paddle_frect.size[1]  # Bottom edge of the paddle
    paddle_speed = 1  # Paddle speed from the game's parameters
    paddle_middle_y = table_size[1] / 2  # Middle of the board

    # Check if the paddle is on the left or right side of the table
    is_left_paddle = paddle_x < table_size[0] / 2

    # Estimate ball velocity
    if previous_ball_position is None:
        ball_velocity = (0, 0)  # Default velocity on the first frame
    else:
        ball_velocity = (
            ball_frect.pos[0] - previous_ball_position[0],
            ball_frect.pos[1] - previous_ball_position[1],
        )

    # Update the global previous ball position
    previous_ball_position = ball_frect.pos

    # Detect if the AI just hit the ball
    if is_left_paddle and ball_velocity[0] > 0 and paddle_x < ball_frect.pos[0] < paddle_x + paddle_frect.size[0]:
        ball_last_hit_by_ai = True
    elif not is_left_paddle and ball_velocity[0] < 0 and paddle_x < ball_frect.pos[0] < paddle_x + paddle_frect.size[0]:
        ball_last_hit_by_ai = True
    else:
        ball_last_hit_by_ai = False

    # Return to the middle of the board after hitting the ball
    if ball_last_hit_by_ai:
        if paddle_top_edge + paddle_frect.size[1] / 2 < paddle_middle_y:
            return "down"
        elif paddle_top_edge + paddle_frect.size[1] / 2 > paddle_middle_y:
            return "up"
        else:
            return None  # Already at the center

    # Helper function to predict ball position
    def predict_ball_y(ball_frect, ball_velocity, table_size, paddle_x):
        ball_x, ball_y = ball_frect.pos
        vx, vy = ball_velocity
        height = table_size[1]

        # Prevent division by zero if the ball is stationary or moving vertically
        if vx == 0:
            return ball_y

        # Time to reach the paddle's x-plane
        time_to_paddle = (paddle_x - ball_x) / vx

        if time_to_paddle < 0:
            return None  # Ball is moving away from the paddle

        # Predicted y-position of the ball
        predicted_y = ball_y + vy * time_to_paddle

        # Handle wall bounces within the table's vertical bounds
        while predicted_y < 0 or predicted_y > height:
            if predicted_y < 0:
                predicted_y = -predicted_y  # Reflect off the top wall
            elif predicted_y > height:
                predicted_y = 2 * height - predicted_y  # Reflect off the bottom wall

        return predicted_y

    # Predict the ball's intersection y-coordinate with the paddle's plane
    target_y = predict_ball_y(ball_frect, ball_velocity, table_size, paddle_x)

    # If the ball is approaching the paddle, aim for a corner hit
    if target_y is not None:
        # Ensure the paddle does not exceed the table's boundaries
        target_top_limit = paddle_top_edge + 3
        target_bottom_limit = paddle_bottom_edge - 3

        if target_y < target_top_limit:  # Aim for the top edge
            return "up"
        elif target_y > target_bottom_limit:  # Aim for the bottom edge
            return "down"
        else:
            # Default to aligning with the ball
            if paddle_top_edge + paddle_frect.size[1] / 2 < target_y:
                return "down"
            elif paddle_top_edge + paddle_frect.size[1] / 2 > target_y:
                return "up"
            else:
                return None  # Paddle is already aligned

    # Default behavior: no movement
    return None
