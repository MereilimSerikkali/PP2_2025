import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display (not needed for audio, but required for Pygame)
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Music Player")

# Initialize Pygame mixer for audio
pygame.mixer.init()

# Load music tracks (add paths to your music files)
music_dir = "music"  # Directory containing music files
tracks = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
current_track = 0

# Function to load and play a track
def play_track(index):
    if 0 <= index < len(tracks):
        pygame.mixer.music.load(tracks[index])
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(tracks[index])}")
    else:
        print("No more tracks.")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

# Function to play next track
def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_track(current_track)

# Function to play previous track
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_track(current_track)

# Main loop
running = True
paused = False
play_track(current_track)  # Start playing the first track

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("Music paused.")
                else:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                        print("Music resumed.")
                    else:
                        play_track(current_track)
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next track
                next_track()
            elif event.key == pygame.K_b:  # Previous track
                previous_track()

# Quit Pygame
pygame.quit()