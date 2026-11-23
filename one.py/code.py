import pygame
import random
import sys
import argparse

# Game settings
WIDTH = 400
HEIGHT = 600
BIRD_X = 100
BIRD_SIZE = 30
GRAVITY = 1
JUMP_VELOCITY = -10
PIPE_WIDTH = 60
PIPE_GAP = 150
GROUND_Y = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 180, 255)
GREEN = (0, 180, 0)
YELLOW = (255, 220, 0)
BLACK = (0, 0, 0)


# -------------------------------
# Bird Physics
# -------------------------------

def update_bird(y, velocity, space_pressed=False):

    if space_pressed:
        velocity = JUMP_VELOCITY

    velocity += GRAVITY
    y += velocity

    return y, velocity


# -------------------------------
# Collision Detection
# -------------------------------

def check_collision(y):

    if y < 0:
        return True

    if y + BIRD_SIZE >= GROUND_Y:
        return True

    return False


# -------------------------------
# Pipe Scoring
# -------------------------------

def check_score(pipe_x, pipe_width, bird_x, score):

    if pipe_x + pipe_width < bird_x:
        score += 1
        return score, True

    return score, False


# -------------------------------
# Test Cases
# -------------------------------

def run_tests():

    print("\n===== FLAPPY BIRD TEST CASES =====\n")

    # TEST CASE 1: Normal Input

    print("TEST CASE 1: Normal Input")

    y = 300
    velocity = 0

    for frame in range(1, 3):

        y, velocity = update_bird(y, velocity)

        print(
            f"Frame {frame}: "
            f"velocity={velocity}, y={y}"
        )

    assert (y, velocity) == (303, 2)

    print("Test Case 1: PASSED\n")


    # TEST CASE 2: Boundary Input

    print("TEST CASE 2: Boundary Input")

    # Part A: Ground Collision

    y = 570

    if check_collision(y):
        print("Ground Collision: Game Over")

    # Part B: Top Boundary

    y = 5
    velocity = 0

    y, velocity = update_bird(
        y, velocity, space_pressed=True
    )

    print(f"Velocity={velocity}, y={y}")

    if check_collision(y):
        print("Bird left the top: Game Over")

    assert (y, velocity) == (-4, -9)

    print("Test Case 2: PASSED\n")


    # TEST CASE 3: Invalid Input

    print("TEST CASE 3: Invalid Input")

    y = 300
    velocity = 0

    # Z key is not SPACE, so no jump occurs.
    y, velocity = update_bird(y, velocity)

    print(f"Key ignored: velocity={velocity}, y={y}")

    assert (y, velocity) == (301, 1)

    print("Test Case 3: PASSED\n")


    # TEST CASE 4: Different Valid Scenario

    print("TEST CASE 4: Different Valid Scenario")

    # Part A: Bird jumps

    y = 300
    velocity = 5

    y, velocity = update_bird(
        y, velocity, space_pressed=True
    )

    print(f"Velocity={velocity}, y={y}")

    assert (y, velocity) == (291, -9)

    # Part B: Pipe passed

    score = 0

    score, passed = check_score(
        pipe_x=39,
        pipe_width=60,
        bird_x=100,
        score=score
    )

    if passed:
        print(f"Pipe passed! Score: {score}")

    assert score == 1

    print("Test Case 4: PASSED\n")

    print("ALL TEST CASES PASSED!")


# -------------------------------
# Main Game
# -------------------------------

def start_game():

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Bird Clone")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 40)

    bird_y = 300
    velocity = 0

    score = 0
    game_over = False

    pipes = []

    def create_pipe():

        gap_y = random.randint(200, 400)

        pipes.append({
            "x": WIDTH,
            "gap_y": gap_y,
            "scored": False
        })

    create_pipe()

    running = True

    while running:

        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if game_over:

                        bird_y = 300
                        velocity = 0
                        score = 0
                        pipes.clear()
                        create_pipe()
                        game_over = False

                    else:
                        velocity = JUMP_VELOCITY

        if not game_over:

            # Apply gravity
            bird_y, velocity = update_bird(
                bird_y, velocity
            )

            # Move pipes
            for pipe in pipes:

                pipe["x"] -= 3

            # Create new pipes
            if pipes[-1]["x"] < 200:
                create_pipe()

            # Remove old pipes
            pipes = [
                p for p in pipes
                if p["x"] + PIPE_WIDTH > 0
            ]

            # Bird rectangle
            bird_rect = pygame.Rect(
                BIRD_X,
                bird_y,
                BIRD_SIZE,
                BIRD_SIZE
            )

            # Boundary collision
            if check_collision(bird_y):
                game_over = True

            # Pipe collision and scoring
            for pipe in pipes:

                top_height = pipe["gap_y"] - PIPE_GAP // 2
                bottom_y = pipe["gap_y"] + PIPE_GAP // 2

                top_pipe = pygame.Rect(
                    pipe["x"],
                    0,
                    PIPE_WIDTH,
                    top_height
                )

                bottom_pipe = pygame.Rect(
                    pipe["x"],
                    bottom_y,
                    PIPE_WIDTH,
                    HEIGHT - bottom_y
                )

                if bird_rect.colliderect(top_pipe):
                    game_over = True

                if bird_rect.colliderect(bottom_pipe):
                    game_over = True

                # Increase score
                if not pipe["scored"]:

                    if pipe["x"] + PIPE_WIDTH < BIRD_X:
                        score += 1
                        pipe["scored"] = True

        # Draw background
        screen.fill(BLUE)

        # Draw pipes
        for pipe in pipes:

            top_height = pipe["gap_y"] - PIPE_GAP // 2
            bottom_y = pipe["gap_y"] + PIPE_GAP // 2

            pygame.draw.rect(
                screen,
                GREEN,
                (pipe["x"], 0, PIPE_WIDTH, top_height)
            )

            pygame.draw.rect(
                screen,
                GREEN,
                (
                    pipe["x"],
                    bottom_y,
                    PIPE_WIDTH,
                    HEIGHT - bottom_y
                )
            )

        # Draw bird
        pygame.draw.circle(
            screen,
            YELLOW,
            (BIRD_X + 15, int(bird_y) + 15),
            15
        )

        # Draw score
        score_text = font.render(
            f"Score: {score}", True, WHITE
        )

        screen.blit(score_text, (10, 10))

        if game_over:

            text = font.render(
                "GAME OVER", True, WHITE
            )

            restart = pygame.font.SysFont(
                None, 25
            ).render(
                "Press SPACE to Restart",
                True,
                WHITE
            )

            screen.blit(text, (110, 250))
            screen.blit(restart, (90, 300))

        pygame.display.update()

    pygame.quit()
    sys.exit()


# -------------------------------
# Program Execution
# -------------------------------

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run all test cases"
    )

    args = parser.parse_args()

    if args.test:
        run_tests()
    else:
        start_game()
