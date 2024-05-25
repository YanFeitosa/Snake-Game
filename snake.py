from config import *

class Snake:
    def __init__(self, cell_size, snake_size):
        self.size = snake_size  # Number of segments in the snake
        self.cell_size = cell_size  # Size of each cell
        self.segments = self.spawn_position()  # Snake segments
        self.head = self.segments[0]  # Head of the snake
        self.direction = (1, 0)  # Initially moving right
        self.growing = False  # Flag to indicate if the snake is growing

    def move(self):
        # Update the position of the snake's head based on the current direction
        new_head = (self.head[0] + self.direction[0] * self.cell_size, self.head[1] + self.direction[1] * self.cell_size)

        if self.growing:
            self.segments = [new_head] + self.segments  # Add a new segment to the snake
            self.growing = False  # Reset the growing flag
        else:
            self.segments = [new_head] + self.segments[:-1]  # Move the snake by updating its segments
            self.head = self.segments[0]  # Update the head of the snake

    def change_direction(self, direction):
        # Change the direction of the snake based on user input
        if direction == 'UP' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'DOWN' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == 'LEFT' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == 'RIGHT' and self.direction != (-1, 0):
            self.direction = (1, 0)

    def spawn_position(self):
        # Determine the initial position of the snake
        cells_count = SCREEN_WIDTH // self.cell_size
        center_cell_index = cells_count // 2
        center_y = center_cell_index * self.cell_size + 100  # Vertical adjustment to fit within the playable area
        segments = [(center_cell_index * self.cell_size, center_y)]
        
        # Add additional segments if the snake size is greater than 1
        if self.size > 1:
            for i in range(1, self.size):
                new_segment_x = (center_cell_index - i) * self.cell_size
                segments.append((new_segment_x, center_y))

        return segments

    def grow(self):
        # Increase the size of the snake by adding a new segment
        self.growing = True
        self.size += 1

    def check_collisions(self):
        # Check if the snake has collided with the wall or itself
        self.head = self.segments[0]
        if (
            self.head[0] < 0
            or self.head[0] >= SCREEN_WIDTH
            or self.head[1] < 100
            or self.head[1] >= SCREEN_HEIGHT
        ):
            return True  # Collision with the wall
        if len(set(self.segments)) < len(self.segments):
            return True  # Collision with itself
        return False

    def draw(self, screen):
        # Draw the snake on the screen
        for segment in self.segments:
            if segment == self.segments[0]:  # Head of the snake
                pygame.draw.rect(screen, DARK_GREEN, (segment[0], segment[1], self.cell_size, self.cell_size))
            else:  # Body segments of the snake
                pygame.draw.rect(screen, GREEN, (segment[0], segment[1], self.cell_size, self.cell_size))
