from config import *

class GameOverScreen:
    def __init__(self, game):
        self.game = game  # Reference to the main game object
        self.screen = game.screen  # Pygame screen object

    def handle_events(self):
        # Handle events in the game over screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from menu_screen import MenuScreen
                    self.game.change_screen(MenuScreen(self.game))  # Switch to menu screen on ESC key press
                elif event.key == pygame.K_SPACE:
                    # Reset score and switch to game screen on SPACE key press
                    self.game.score = 0
                    self.game.fps = self.game.ingame_fps
                    from game_screen import GameScreen
                    self.game.change_screen(GameScreen(self.game))

    def update(self):
        # Update the game over screen (unused)
        pass

    def render(self):
        # Render the game over screen
        self.screen.fill(BLACK)  # Clear the screen
        self.game.blit_text("GAME OVER", 120, RED,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 2 // 12, 'center')  # Render "GAME OVER" text
        self.game.blit_text(f"HIGHSCORE: {self.game.highscore}", 44, YELLOW, self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 3 // 12, 'center')  # Render high score
        self.game.blit_text(f"LAST SCORE: {self.game.score}", 32, LIGHT_GRAY, self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 4 // 12, 'center')  # Render last score
        self.game.blit_text("Press SPACE to try again", 26, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 7 // 12, 'center')  # Render instruction to try again
        self.game.blit_text("Press ESC to go back to MENU", 26, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 8 // 12, 'center')  # Render instruction to go back to menu
        pygame.display.update()  # Update the display
