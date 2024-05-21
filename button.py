import pygame

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, scale_factor=1.1):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.original_image = self.image if self.image else self.text
        self.rect = self.original_image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.scale_factor = scale_factor

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if self.rect.collidepoint(position):
            return True
        return False

    def changeColor(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def scaleUp(self, position):
        if self.rect.collidepoint(position):
            if self.image:
                self.image = pygame.transform.scale(self.original_image, 
                            (int(self.rect.width * self.scale_factor), int(self.rect.height * self.scale_factor)))
            else:
                # If there is no image, use the text size as the rect size
                self.image = pygame.Surface((self.text_rect.width, self.text_rect.height))
                self.image.fill((0, 0, 0, 0))  # Create a transparent surface

            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            larger_font = pygame.font.Font("Assets/mainmenu/font.ttf", int(self.font.get_height() * self.scale_factor))
            self.text = larger_font.render(self.text_input, True, self.hovering_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
