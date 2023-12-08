import pygame

class Player:
    def __init__(self, x_coordinate, y_coordinate, screen, width, height) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.screen = screen
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x_coordinate, self.y_coordinate, self.width, self.height))



        