from checkbox import *

class SettingsScreen:
    def __init__(self, game):
        self.game = game  # Reference to the main game object
        self.screen = game.screen

        # Variables to control the selected options
        self.selected_grid = 1  # Index of the selected grid option
        self.selected_speed = 0  # Index of the selected speed option
        self.selected_length = 1  # Index of the selected snake length option

        # Lists of options for each category
        self.grid_options = ["10x10", "12x12", "20x20"]
        self.speed_options = ["1", "1.5", "2"]
        self.length_options = ["1", "3", "5"]

        # Lists of checkboxes for each category
        self.grid_checkboxes = []
        self.speed_checkboxes = []
        self.length_checkboxes = []

        # Create checkboxes for grid options
        for i, option in enumerate(self.grid_options):
            checkbox = CheckBox(option, (SCREEN_WIDTH * i // 3 + 120, SCREEN_HEIGHT * 4 // 12), 24, checked=False)
            self.grid_checkboxes.append(checkbox)

        # Create checkboxes for speed options
        for i, option in enumerate(self.speed_options):
            checkbox = CheckBox(option, (SCREEN_WIDTH * i // 3 + 120, SCREEN_HEIGHT * 6 // 12), 24, checked=False)
            self.speed_checkboxes.append(checkbox)

        # Create checkboxes for snake length options
        for i, option in enumerate(self.length_options):
            checkbox = CheckBox(option, (SCREEN_WIDTH * i // 3 + 120, SCREEN_HEIGHT * 8 // 12), 24, checked=False)
            self.length_checkboxes.append(checkbox)

    def handle_events(self):
        # Handle events in the settings screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from menu_screen import MenuScreen
                    self.game.change_screen(MenuScreen(self.game))  # Switch to menu screen on ESC key press
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_checkbox_clicks()

    def handle_checkbox_clicks(self):
        # Handle checkbox clicks
        mouse_pos = pygame.mouse.get_pos()

        # Check if a grid checkbox was clicked
        for i, checkbox in enumerate(self.grid_checkboxes):
            checkbox.handle_click(mouse_pos)
            if checkbox.checked:
                for _checkbox in self.grid_checkboxes:
                    _checkbox.checked = False
                checkbox.checked = True
                self.selected_grid = i

        # Check if a speed checkbox was clicked
        for i, checkbox in enumerate(self.speed_checkboxes):
            checkbox.handle_click(mouse_pos)
            if checkbox.checked:
                for _checkbox in self.speed_checkboxes:
                    _checkbox.checked = False
                checkbox.checked = True
                self.selected_speed = i

        # Check if a snake length checkbox was clicked
        for i, checkbox in enumerate(self.length_checkboxes):
            checkbox.handle_click(mouse_pos)
            if checkbox.checked:
                for _checkbox in self.length_checkboxes:
                    _checkbox.checked = False
                checkbox.checked = True
                self.selected_length = i        

    def update(self):
        # Update game parameters based on selected options
        if self.selected_grid == 0:
            self.game.cell_size = 60
        elif self.selected_grid == 1:
            self.game.cell_size = 50
        elif self.selected_grid == 2:
            self.game.cell_size = 30 

        if self.selected_speed == 0:
            self.game.ingame_fps = 10
        elif self.selected_speed == 1:
            self.game.ingame_fps = 15   
        elif self.selected_speed == 2:
            self.game.ingame_fps = 20

        if self.selected_length == 0:
            self.game.snake_size = 1
        if self.selected_length == 1:
            self.game.snake_size = 3
        if self.selected_length == 2:
            self.game.snake_size = 5

    def render(self):
        # Render the settings screen
        self.screen.fill(BLACK)
        self.game.blit_text("SETTINGS", 120, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 1 // 12, 'center')

        # Draw checkboxes for grid options
        self.game.blit_text("GRID", 44, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 3 // 12, 'center')
        for checkbox in self.grid_checkboxes:
            checkbox.draw(self.screen)
        
        # Draw checkboxes for speed options
        self.game.blit_text("SPEED", 44, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 5 // 12, 'center')
        for checkbox in self.speed_checkboxes:
            checkbox.draw(self.screen)
        
        # Draw checkboxes for snake length options
        self.game.blit_text("SNAKE LENGTH", 44, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 7 // 12, 'center')
        for checkbox in self.length_checkboxes:
            checkbox.draw(self.screen)

        # Render instruction to go back to menu
        self.game.blit_text("Press ESC to go back to MENU", 26, WHITE,  self.screen, SCREEN_WIDTH // 2 , SCREEN_HEIGHT * 10 // 12, 'center')
        pygame.display.update()  # Update the display
