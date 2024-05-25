from config import *
import random

class Apple:
    def __init__(self, cell_size, snake):
        self.cell_size = cell_size  # Size of each cell
        self.radius = self.cell_size // 2  # Radius of the apple
        self.spawn(snake)  # Spawn the apple at a random position

    def generate_position(self):
        # Generate a random position for the apple within the game area
        while True:
            self.fail = False
            x = random.randint(0, SCREEN_WIDTH // self.cell_size - 1) * self.cell_size + self.radius
            y = random.randint(0, SCREEN_WIDTH // self.cell_size - 1) * self.cell_size + self.radius + 100  # Add an offset to ensure the apple spawns within the playable area
            # Check if the generated position for the apple does not collide with any segment of the snake
            if (x - self.radius, y - self.radius) not in self.snake.segments:
                return x, y
    def spawn(self, snake):
        self.snake = snake
        # Spawn the apple at a random position
        self.position = self.generate_position()

    def draw(self, screen):
        # Draw the apple on the screen
        pygame.draw.circle(screen, RED, self.position, self.radius)
