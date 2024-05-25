from config import *
from game_over_screen import GameOverScreen
from snake import Snake
from apple import Apple

class GameScreen:
    def __init__(self, game):
        self.game = game  # Reference to the main game object
        self.screen = game.screen  # Pygame screen object
        self.font = pygame.font.Font(None, 52)  # Font for rendering text
        self.direction = 'RIGHT'  # Initial direction of the snake
        self.snake = Snake(self.game.cell_size, self.game.snake_size)  # Initialize the snake object
        self.apple = Apple(self.game.cell_size, self.snake)  # Initialize the apple object

    def handle_events(self):
        # Handle user input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Update the direction based on arrow keys or WASD keys
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.direction = 'DOWN'
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.direction = 'UP'
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.direction = 'RIGHT'
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.direction = 'LEFT'

    def update(self):
        # Update the game state
        snake_head_rect = pygame.Rect(self.snake.head[0], self.snake.head[1], self.game.cell_size, self.game.cell_size)
        
        # Check if the snake has collided with the apple
        if snake_head_rect.collidepoint(self.apple.position):
            self.snake.grow()
            self.apple.spawn(self.snake)
            self.game.score += 1
            self.game.apple_sound.play()
            if self.game.score > self.game.highscore:
                self.game.highscore = self.game.score

        # Check for collisions with walls or itself
        if self.snake.check_collisions():
            self.game_over()
        
        # Update snake direction and movement
        self.snake.change_direction(self.direction)
        self.snake.move()

    def render(self):
        # Render the game screen
        self.screen.fill(BLACK)  # Clear the screen
        pygame.draw.rect(self.screen, DARK_GRAY, (0, 100, SCREEN_WIDTH, SCREEN_WIDTH))  # Draw game area
        self.apple.draw(self.screen)  # Draw the apple
        self.snake.draw(self.screen)  # Draw the snake
        pygame.draw.rect(self.screen, LIGHT_GRAY, (0, 0, SCREEN_WIDTH, 100))  # Draw top panel
        self.game.blit_text(f"SCORE: {self.game.score}", 50, WHITE, self.screen, SCREEN_WIDTH // 2 , 25, 'center')  # Render score
        self.game.blit_text(f"HIGHSCORE: {self.game.highscore}", 32, YELLOW, self.screen, SCREEN_WIDTH // 2 , 75, 'center')  # Render high score
        pygame.display.update()  # Update the display

    def game_over(self):
        # Handle game over event
        self.game.game_over_sound.play()  # Play game over sound
        if self.game.score == self.game.highscore:
            # Update high score if necessary
            with open('files/highscore.txt', 'w') as highscore:
                highscore.write(str(self.game.score))
        self.game.fps = 120  # Reset FPS
        self.game.change_screen(GameOverScreen(self.game))  # Switch to game over screen
