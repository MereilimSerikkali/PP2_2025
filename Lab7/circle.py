import pygame
pygame.init()

# display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move the Red Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 25
ball_diameter = ball_radius * 2
ball_x = (screen_width - ball_diameter) // 2  # Start at the center of the screen
ball_y = (screen_height - ball_diameter) // 2
ball_speed = 20  # Pixels to move per key press

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move up, but ensure the ball doesn't leave the screen
                if ball_y - ball_speed >= 0:
                    ball_y -= ball_speed
            elif event.key == pygame.K_DOWN:
                # Move down, but ensure the ball doesn't leave the screen
                if ball_y + ball_diameter + ball_speed <= screen_height:
                    ball_y += ball_speed
            elif event.key == pygame.K_LEFT:
                # Move left, but ensure the ball doesn't leave the screen
                if ball_x - ball_speed >= 0:
                    ball_x -= ball_speed
            elif event.key == pygame.K_RIGHT:
                # Move right, but ensure the ball doesn't leave the screen
                if ball_x + ball_diameter + ball_speed <= screen_width:
                    ball_x += ball_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x + ball_radius, ball_y + ball_radius), ball_radius)

    # Update the display
    pygame.display.flip()

pygame.quit()