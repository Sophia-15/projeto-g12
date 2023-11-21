import pygame
import random

pygame.init()

white = (255, 255, 255)
blue = (0, 0, 255)
orange = (255, 165, 0)
yellow = (255, 255, 0)
width = 1000
height = 900

display = pygame.display.set_mode([width, height])
pygame.display.set_caption('Infinite Runner')

background = (0,0,0)
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
timer = pygame.time.Clock()


player_x = 50
player_y = 200
y_change = 0
x_change = 0
gravity = 1.2
obstacles = [300, 450, 600]
obstacles_speed = 3
active = True
score = 0

running = True
while running:
    timer.tick(fps)
    display.fill(background)
    floor = pygame.draw.rect(display, white, [0, 220, width, 5])
    player = pygame.draw.rect(display, (255,0,0), [player_x, player_y, 20, 20])
    obstacles0 = pygame.draw.rect(display, blue, [obstacles[0], 200, 20, 20])
    obstacles1 = pygame.draw.rect(display, orange, [obstacles[1], 200, 20, 20])
    obstacles2 = pygame.draw.rect(display, yellow, [obstacles[2], 200, 20, 20])
    score_text = font.render(f'Score: {score}', True, white, (0,0,0))
    display.blit(score_text, (1, 1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_change == 0:
                y_change = 16
            if event.key == pygame.K_RIGHT:
                x_change = 4
            if event.key == pygame.K_LEFT:
                x_change = -4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0

    for i in range(len(obstacles)):
        if active:
            obstacles[i] -=obstacles_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
                if obstacles1.colliderect(obstacles0) or obstacles1.colliderect(obstacles2):
                    obstacles[i] = random.randint(470, 570)
                if obstacles2.colliderect(obstacles0) or obstacles2.colliderect(obstacles1):
                    obstacles[i] = random.randint(470, 570)
                if obstacles0.colliderect(obstacles1) or obstacles2.colliderect(obstacles2):
                    obstacles[i] = random.randint(470, 570)
            if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2):
                active = False

    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    if score > 15:
        obstacles_speed = 4
    if score > 30:
        obstacles_speed = 5
    if score > 60:
        obstacles_speed = 6

    if active == False:
        display.fill(background)
        result_text = font.render(f'Score final: {score}', True, white, (0,0,0))
        instfim_text = font.render(f'Aperte espaço para fechar o jogo', True, white, (0,0,0))
        display.blit(result_text, (150, 120))
        display.blit(instfim_text, (70, 140))
        if event.key == pygame.K_SPACE:
                running = False
    pygame.display.flip()
pygame.quit()