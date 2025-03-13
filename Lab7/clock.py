import pygame
import time
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)

# Load images
clock_face = pygame.image.load("clock.png")
minute_hand = pygame.image.load("min_hand.png")
second_hand = pygame.image.load("sec_hand.png")

# Scale images
clock_face = pygame.transform.scale(clock_face, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (100, 10))
second_hand = pygame.transform.scale(second_hand, (120, 10))

def blitRotate(surf, image, pos, originPos, angle):
    if not isinstance(surf, pygame.Surface):
        print("Error: surf is not a valid pygame.Surface")
        return

    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    print("Blitting at:", rotated_image_rect.topleft)
    surf.blit(rotated_image, rotated_image_rect)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(clock_face, (0, 0))
    
    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    # Calculate angles
    second_angle = -seconds * 6  # 360 degrees / 60 seconds
    minute_angle = -minutes * 6   # 360 degrees / 60 minutes
    
    # Draw hands
    blitRotate(screen, minute_hand, CENTER, (10, 5), minute_angle)
    blitRotate(screen, second_hand, CENTER, (10, 5), second_angle)
    
    pygame.display.flip()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

