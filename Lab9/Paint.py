import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Color definitions
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
colors = [black, red, green, blue, yellow, purple]

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Enhanced Paint Application")
screen.fill(white)

# Game clock
clock = pygame.time.Clock()

# Drawing variables
drawing = False
last_pos = None
tool = "pencil"  # Current tool (pencil, eraser, rectangle, circle)
radius = 5       # Brush size
current_color = black
fill_mode = False  # Whether shapes should be filled

# Font for UI
font = pygame.font.SysFont('Arial', 16)

def draw_line(surface, color, start_pos, end_pos, width):
    """Draw a smooth line between two points"""
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start_pos[0] + float(i) / distance * dx)
        y = int(start_pos[1] + float(i) / distance * dy)
        pygame.draw.circle(surface, color, (x, y), width)

def draw_rectangle(surface, color, start_pos, end_pos, fill=False):
    """Draw a rectangle between two points"""
    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    if fill:
        pygame.draw.rect(surface, color, (x, y, width, height))
    else:
        pygame.draw.rect(surface, color, (x, y, width, height), 2)

def draw_circle(surface, color, start_pos, end_pos, fill=False):
    """Draw a circle with center at start_pos and radius to end_pos"""
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    radius = int((dx**2 + dy**2)**0.5)
    if fill:
        pygame.draw.circle(surface, color, start_pos, radius)
    else:
        pygame.draw.circle(surface, color, start_pos, radius, 2)

def draw_ui():
    """Draw the user interface with tool and color information"""
    # Draw tool information
    tool_text = font.render(f"Tool: {tool}", True, black)
    screen.blit(tool_text, (10, 10))
    
    # Draw color information
    color_text = font.render(f"Color: {current_color}", True, black)
    screen.blit(color_text, (10, 30))
    
    # Draw brush size
    size_text = font.render(f"Brush Size: {radius}", True, black)
    screen.blit(size_text, (10, 50))
    
    # Draw fill mode
    fill_text = font.render(f"Fill: {'ON' if fill_mode else 'OFF'}", True, black)
    screen.blit(fill_text, (10, 70))
    
    # Draw color palette
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (700, 10 + i*30, 25, 25))
        if color == current_color:
            pygame.draw.rect(screen, black, (700, 10 + i*30, 25, 25), 2)

def clear_screen():
    """Clear the drawing area"""
    screen.fill(white)

# Main game loop
running = True
start_pos = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Mouse button down events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                drawing = True
                last_pos = event.pos
                start_pos = event.pos
                
                # Check if color palette was clicked
                for i, color in enumerate(colors):
                    if 700 <= event.pos[0] <= 725 and 10 + i*30 <= event.pos[1] <= 35 + i*30:
                        current_color = color
            
            elif event.button == 4:  # Mouse wheel up - increase brush size
                radius = min(50, radius + 1)
            elif event.button == 5:  # Mouse wheel down - decrease brush size
                radius = max(1, radius - 1)
        
        # Mouse button up events
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left click release
                drawing = False
                if tool == "rectangle" and start_pos:
                    draw_rectangle(screen, current_color, start_pos, event.pos, fill_mode)
                elif tool == "circle" and start_pos:
                    draw_circle(screen, current_color, start_pos, event.pos, fill_mode)
                start_pos = None
        
        # Mouse motion events
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if tool == "pencil":
                    draw_line(screen, current_color, last_pos, event.pos, radius)
                elif tool == "eraser":
                    draw_line(screen, white, last_pos, event.pos, radius)
                last_pos = event.pos
        
        # Keyboard events
        if event.type == pygame.KEYDOWN:
            # Tool selection
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_p:
                tool = "pencil"
            elif event.key == pygame.K_f:
                fill_mode = not fill_mode  # Toggle fill mode
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                radius = min(50, radius + 1)  # Increase brush size
            elif event.key == pygame.K_MINUS:
                radius = max(1, radius - 1)  # Decrease brush size
            elif event.key == pygame.K_SPACE:
                clear_screen()  # Clear the screen
            
            # Color selection (number keys 1-6)
            if pygame.K_1 <= event.key <= pygame.K_6:
                index = event.key - pygame.K_1
                if index < len(colors):
                    current_color = colors[index]
    
    # Draw the UI
    draw_ui()
    
    # Update the display
    pygame.display.update()
    clock.tick(60)