import pygame
from players import *
from ball import *
from points import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=True)

player1 = Player(0 ,200, screen, 20, 120)
player2 = Player(770, 200, screen, 20, 120)

score = Score()
ball = Ball(385, 385, screen, 0.25, 0.25)

run = False


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()

    #movement for player 1
    if keys[pygame.K_w]:
        player1.y_coordinate -= 0.5
        player1.y_coordinate = max(player1.y_coordinate, 0)
    if keys[pygame.K_s]:
        player1.y_coordinate += 0.5
        player1.y_coordinate = min(player1.y_coordinate, SCREEN_HEIGHT - player1.height)
    
    #movement for player 2
    if keys[pygame.K_UP]:
        player2.y_coordinate -= 0.5
        player2.y_coordinate = max(player2.y_coordinate, 0)
    if keys[pygame.K_DOWN]:
        player2.y_coordinate += 0.5
        player2.y_coordinate = min(player2.y_coordinate, SCREEN_HEIGHT - player2.height)
    
    screen.fill((0, 0, 0))

    
    player1.draw()
    player2.draw()
    ball.draw()


    ball.update(player1, player2, SCREEN_WIDTH, SCREEN_HEIGHT, score)


    score_text = font.render(score.get_score_text(), True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))


    pygame.display.flip()

pygame.quit
