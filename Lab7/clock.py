import pygame
import math
from datetime import datetime
pygame.init()

# Set up display (smaller screen)
screen_width, screen_height = 230, 230  # Smaller screen size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

# Load images
clock_face = pygame.image.load('clock.png')
minute_hand = pygame.image.load('min_hand.png')
second_hand = pygame.image.load('min_hand.png')  # Assuming same image for simplicity

# Scale down the images (adjust the scale factor as needed)
scale_factor = 0.5  # Reduce size to 50%
clock_face = pygame.transform.scale(clock_face, (int(clock_face.get_width() * scale_factor), int(clock_face.get_height() * scale_factor)))
minute_hand = pygame.transform.scale(minute_hand, (int(minute_hand.get_width() * scale_factor), int(minute_hand.get_height() * scale_factor)))
second_hand = pygame.transform.scale(second_hand, (int(second_hand.get_width() * scale_factor), int(second_hand.get_height() * scale_factor)))

# Get the center of the screen
center_x = screen_width // 2
center_y = screen_height // 2

# Function to rotate an image around its center
def rotate_image(image, angle):
    # Rotate the image
    rotated_image = pygame.transform.rotate(image, angle)
    # Get the rect of the original image
    orig_rect = image.get_rect()
    # Get the rect of the rotated image
    rot_rect = rotated_image.get_rect(center=orig_rect.center)
    # Return the rotated image and its rect
    return rotated_image, rot_rect

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Calculate angles
    minute_angle = (minutes * 7)  # Add 30 degrees to move forward by 5 minutes
    second_angle = (seconds / 60) * 360  # Each second corresponds to 6 degrees

    # Rotate hands
    rotated_minute_hand, minute_rect = rotate_image(minute_hand, -minute_angle)
    rotated_second_hand, second_rect = rotate_image(second_hand, -second_angle)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw clock face (centered)
    clock_face_rect = clock_face.get_rect(center=(center_x, center_y))
    screen.blit(clock_face, clock_face_rect)

    # Draw hands (centered)
    screen.blit(rotated_minute_hand, minute_rect.move(center_x - minute_rect.center[0], center_y - minute_rect.center[1]))
    screen.blit(rotated_second_hand, second_rect.move(center_x - second_rect.center[0], center_y - second_rect.center[1]))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()