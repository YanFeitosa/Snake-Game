from config import *

class MenuScreen:
    def __init__(self, game):
        self.game = game  # Reference to the main game object
        self.game.menu_background_music.play()  # Play the menu background music
        self.screen = game.screen  # Reference to the game's screen

    def handle_events(self):
        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle the quit event
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the system
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Start the game when the space key is pressed
                self.game.menu_background_music.stop()  # Stop the menu music
                self.game.score = 0  # Reset the score
                self.game.fps = self.game.ingame_fps  # Set the FPS to in-game FPS
                from game_screen import GameScreen
                self.game.change_screen(GameScreen(self.game))  # Change to the game screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Handle left mouse button click
                    if self.config_rect.collidepoint(pygame.mouse.get_pos()):
                        # Open settings screen if the config icon is clicked
                        self.game.menu_background_music.stop()  # Stop the menu music
                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Set the cursor to arrow
                        from settings_screen import SettingsScreen
                        self.game.change_screen(SettingsScreen(self.game))  # Change to the settings screen

    def update(self):
        # Update the menu screen
        self.mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
        self.config_rect = self.game.config_icon.get_rect()  # Get the rect for the config icon
        self.config_rect.center = (SCREEN_WIDTH - 50, 50)  # Set the center of the config icon
        if self.config_rect.collidepoint(self.mouse_pos):
            # Enlarge the config icon and change cursor if mouse hovers over it
            self.game.config_icon = self.game.config_icon_large
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            # Reset the config icon size and cursor if mouse is not over it
            self.game.config_icon = self.game.config_icon_small
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def render(self):
        # Render the menu screen
        self.screen.fill(BLACK)  # Fill the screen with black color
        # Draw the snake icon in the center of the screen
        self.screen.blit(self.game.snake_icon, (SCREEN_WIDTH // 2 - self.game.snake_icon.get_width() // 2, SCREEN_HEIGHT // 2 - self.game.snake_icon.get_height() // 2))
        # Render the text for instructions, title, and highscore
        self.game.blit_text("Press SPACE to START", 26, WHITE, self.screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5, 'center')
        self.game.blit_text("SNAKE", 120, GREEN, self.screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 1 // 10, 'center')
        self.game.blit_text(f"HIGHSCORE: {self.game.highscore}", 44, YELLOW, self.screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 12, 'center')
        if self.game.score != -1:
            self.game.blit_text(f"LAST SCORE: {self.game.score}", 32, LIGHT_GRAY, self.screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 12, 'center')
        # Draw the config icon
        self.screen.blit(self.game.config_icon, self.config_rect)
        pygame.display.update()  # Update the display
