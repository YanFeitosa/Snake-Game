import pygame.mixer
from menu_screen import MenuScreen
from config import *

class Game:
    def __init__(self):
        pygame.init()  # Initialize all imported Pygame modules
        pygame.mixer.init()  # Initialize the mixer module for sound
        self.load_files()  # Load all necessary files like images and sounds
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set the screen size
        pygame.display.set_caption(TITLE)  # Set the window title
        pygame.display.set_icon(self.snake_icon)  # Set the window icon
        self.clock = pygame.time.Clock()  # Create a clock object to control the frame rate
        self.current_screen = MenuScreen(self)  # Set the initial screen to the menu
        self.score = -1  # Initialize the score
        self.cell_size = 50  # Set the size of each cell in the grid
        self.snake_size = 3  # Set the initial size of the snake
        self.ingame_fps = 10  # Set the frames per second during gameplay
        self.fps = 120  # Set the frames per second for the main loop

    def change_screen(self, new_screen):
        self.current_screen = new_screen  # Change the current screen to a new one

    def blit_text(self, text, font_size, text_color, surface, pos_x, pos_y, reference_point='topleft'):
        # Render text onto the screen at a given position with a specific font size and color
        font = pygame.font.Font(None, font_size)  # Create a font object
        _text = font.render(text, True, text_color)  # Render the text
        text_rect = _text.get_rect(center=(pos_x, pos_y))  # Get the text rectangle
        setattr(text_rect, reference_point, (pos_x, pos_y))  # Set the reference point for positioning
        surface.blit(_text, text_rect)  # Blit the text onto the surface

    def load_files(self):
        # Load sound and image files
        self.menu_background_music = pygame.mixer.Sound('files/sound/menu_background.wav')
        self.apple_sound = pygame.mixer.Sound('files/sound/apple.wav')
        self.game_over_sound = pygame.mixer.Sound('files/sound/game_over.wav')
        self.snake_icon = pygame.image.load('files/image/logo.png')
        self.config_icon = pygame.image.load('files/image/config.png')
        self.config_icon_small = pygame.transform.scale(self.config_icon, (50, 50))  # Resize the icon
        self.config_icon_large = pygame.transform.scale(self.config_icon, (55, 55))  # Resize the icon
        with open('files/highscore.txt', 'r') as highscore:
            self.highscore = int(highscore.read())  # Read the high score from a file

    def run(self):
        # Main game loop
        while True:
            self.current_screen.handle_events()  # Handle input events
            self.current_screen.update()  # Update the game state
            self.current_screen.render()  # Render the current screen
            self.clock.tick(self.fps)  # Maintain the frame rate

def main():
    game = Game()  # Create a new game instance
    game.run()  # Start the game loop

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
