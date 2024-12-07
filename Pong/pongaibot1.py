# Global variable to track the ball's previous position
previous_ball_position = None

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """
    AI logic for the Pong game, strictly based on pongai.py code.
    - paddle_frect: The AI's paddle rectangle (fRect object).
    - other_paddle_frect: The opponent's paddle rectangle (fRect object).
    - ball_frect: The ball's rectangle (fRect object).
    - table_size: Dimensions of the table (width, height).
    """
    global previous_ball_position

    # Paddle parameters
    paddle_x = paddle_frect.pos[0]  # X-coordinate of the paddle's vertical plane
    paddle_center = paddle_frect.pos[1] + paddle_frect.size[1] / 2  # Center of the paddle
    paddle_speed = 1  # Paddle speed from the game's parameters

    # Estimate ball velocity
    if previous_ball_position is None:
        # Default velocity if no previous frame data is available
        ball_velocity = (0, 0)
    else:
        ball_velocity = (
            ball_frect.pos[0] - previous_ball_position[0],
            ball_frect.pos[1] - previous_ball_position[1],
        )

    # Update the global previous ball position
    previous_ball_position = ball_frect.pos

    # Predict the ball's y-coordinate when it reaches the paddle's x-plane
    def predict_ball_y(ball_frect, ball_velocity, table_size, paddle_x):
        ball_x, ball_y = ball_frect.pos
        ball_width, ball_height = ball_frect.size
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

    # Determine movement direction
    if target_y is None:
        return None  # Ball is moving away, no need to move

    if paddle_center < target_y:
        return "down"
    elif paddle_center > target_y:
        return "up"
    else:
        return None  # Paddle is already aligned
