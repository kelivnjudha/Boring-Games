import subprocess
import sys
import pygame
import sys

pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Load font
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)
    return text_rect.width, text_rect.height

def menu(screen):

    FLAPPY = False
    TUBBY = False
    MARIO = False
    clock = pygame.time.Clock()
    running = True
    selected_option = 0

    # Menu options
    menu_options = [
        "Flappy Bird",
        "Tubby-(In development)",
        "snake Game",
        "Exit",
    ]

    executables = [
        "flappy.exe",  # Replace with the correct path to your Flappy Bird .exe or .py file
        "tubby.py",  # Replace with the correct path to your Tubby .exe or .py file
        "snake.exe",  # Replace with the correct path to your Option 3 .exe or .py file
    ]

    # Load and scale background image
    background_image_path = "menu/menu.jpg"  # Replace with your image path
    background_image = pygame.image.load(background_image_path)
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            # Check for arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if menu_options[selected_option] == "Exit":
                        running = False
                        sys.exit()
                    else:
                        # Hide the client_launcher window
                        pygame.display.iconify()

                        # Run the selected executable or python script
                        executable = executables[selected_option]
                        if executable.endswith(".py"):
                            process = subprocess.Popen([sys.executable, executable], creationflags=subprocess.CREATE_NO_WINDOW)
                        else:
                            process = subprocess.Popen([executable], creationflags=subprocess.CREATE_NO_WINDOW)

                        # Wait for the game subprocess to end
                        process.wait()

                        # Restore the client_launcher window
                        screen = pygame.display.set_mode((screen_width, screen_height))

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw menu options
        for i, option in enumerate(menu_options):
            color = blue if i == selected_option else (0, 0, 0)
            draw_text(option, screen_width // 2 - 50, screen_height // 2 - 100 + i * 50, color)

        pygame.display.flip()
        clock.tick(60)

def main():
    client_executable = "dist/client_2.exe"  # Replace with the correct path to your .exe file

    try:
        subprocess.Popen([client_executable], creationflags=subprocess.CREATE_NO_WINDOW)
        menu(screen)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Make sure the path to the client executable is correct: {client_executable}")
        sys.exit(1)

if __name__ == "__main__":
    main()
