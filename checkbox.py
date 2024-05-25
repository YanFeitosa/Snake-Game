from config import *

class CheckBox:
    def __init__(self, text, position, font_size, checked=False):
        self.text = text  # The text displayed next to the checkbox
        self.position = position  # The position of the checkbox
        self.font = pygame.font.Font(None, font_size)  # Font used for rendering text
        self.checked = checked  # Boolean indicating whether the checkbox is checked or not

    def draw(self, surface):
        # Render the text of the checkbox
        text_render = self.font.render(self.text, True, WHITE)
        text_rect = text_render.get_rect(midleft=self.position)

        # Draw the checkbox outline and fill it based on its state
        pygame.draw.rect(surface, GREEN if self.checked else WHITE, (text_rect.left - 40, text_rect.centery - 10, 20, 20), 2)
        surface.blit(text_render, text_rect)  # Blit the text onto the surface

    def handle_click(self, mouse_pos):
        # Check if the checkbox is clicked
        text_render = self.font.render(self.text, True, WHITE)
        text_rect = text_render.get_rect(midleft=self.position)
        checkbox_rect = pygame.Rect(text_rect.left - 40, text_rect.centery - 10, 20, 20)
        
        # Toggle the checkbox state if it's clicked
        if checkbox_rect.collidepoint(mouse_pos):
            self.checked = not self.checked
