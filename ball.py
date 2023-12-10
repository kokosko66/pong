import pygame
import math

class Ball:
    def __init__(self, x, y, screen, initial_velocity_x, initial_velocity_y):
        self.x = x
        self.y = y
        self.screen = screen
        self.velocity_x = initial_velocity_x
        self.velocity_y = initial_velocity_y
        self.radius = 10

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)
    


    def update(self, player1, player2, SCREEN_WIDTH, SCREEN_HEIGHT, score):

        self.x += self.velocity_x
        self.y += self.velocity_y


        if self.x - self.radius <= 0:

            score.increment_player2()  
            self.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.velocity_x = abs(self.velocity_x) 

        elif self.x + self.radius >= SCREEN_WIDTH:

            score.increment_player1()  
            self.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.velocity_x = -abs(self.velocity_x)


        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:

            self.velocity_x *= -1

        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:

            self.velocity_y *= -1


        if (
            player1.x_coordinate < self.x < player1.x_coordinate + player1.width and
            player1.y_coordinate < self.y < player1.y_coordinate + player1.height
        ):

            self.velocity_x = -self.velocity_x
            self.velocity_y = -self.velocity_y

        if (
            player2.x_coordinate < self.x < player2.x_coordinate + player2.width and
            player2.y_coordinate < self.y < player2.y_coordinate + player2.height
        ):
            
            self.velocity_x = -self.velocity_x
            self.velocity_y = -self.velocity_y


        if self.x - self.radius <= 0:

            score.increment_player2()  
            self.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)

        elif self.x + self.radius >= SCREEN_WIDTH:

            score.increment_player1()  
            self.reset_position(SCREEN_WIDTH, SCREEN_HEIGHT)


        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:

            self.velocity_y *= -1

    def reset_position(self, SCREEN_WIDTH, SCREEN_HEIGHT):

        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
    
    

    