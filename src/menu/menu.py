from choose_name import handle_choose_name
import random
import os
import pygame
import sys
TETRIS_PATH = r'C:/Users/acgs_cesar/Desktop/projetos 1/projeto-g12/src/tetris'
sys.path.append(TETRIS_PATH)
from main_tetris import battery_tetris


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

info = pygame.display.Info()
monitor_size = [pygame.display.Info().current_w,
                pygame.display.Info().current_h]

screen = pygame.display.set_mode((monitor_size), pygame.RESIZABLE)
font = pygame.font.Font(
    r'C:\Users\acgs_cesar\Desktop\projetos 1\projeto-g12\src\menu\retro.ttf', 80)
font_sm = pygame.font.Font(
    r'C:\Users\acgs_cesar\Desktop\projetos 1\projeto-g12\src\menu\retro.ttf', 50)
clock = pygame.time.Clock()

def infinity_runner():
  white = (255, 255, 255)
  blue = (0, 0, 255)
  orange = (255, 165, 0)
  yellow = (255, 255, 0)
  purple = (128, 0, 128)
  green = (1, 50, 32)

  display = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
  pygame.display.set_caption('Infinite Runner')

  background = (0,0,0)
  fps = 60
  font = pygame.font.Font(r'C:\Users\acgs_cesar\Desktop\projetos 1\projeto-g12\src\menu\retro.ttf', 20)
  timer = pygame.time.Clock()


  player_x = 50
  player_y = 600
  y_change = 0
  x_change = 0
  gravity = 1.5
  obstacles = [
    random.randint(600, 800), 
    random.randint(1000, 1200), 
    random.randint(1400, 1600), 
    random.randint(1800, 2000),
    random.randint(2200, 2400)
    ]
  obstacles_speed = 6
  active = True
  score = 0
#   while running == False:
#         display.fill(background)
#         menu_inic = font.render(f'Controles: Botão esquerdo para esquerda;/nBotão direito para direita;/nBotão inferior(Espaço) para pular', True, white, (0,0,0))
#         display.blit(menu_inic, (1, 1))
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                         running == True
  running = True
  while running:
        timer.tick(fps)
        display.fill(background)
        floor = pygame.draw.rect(display, white, [0, 650, monitor_size[0], 10])
        player = pygame.draw.rect(display, (255,0,0), [player_x, player_y, 50, 50])
        obstacles0 = pygame.draw.rect(display, blue, [obstacles[0], 600, 50, 50])
        obstacles1 = pygame.draw.rect(display, orange, [obstacles[1], 600, 50, 50])
        obstacles2 = pygame.draw.rect(display, yellow, [obstacles[2], 600, 50, 50])
        obstacles3 = pygame.draw.rect(display, purple, [obstacles[3], 600, 50, 50])
        obstacles4 = pygame.draw.rect(display, green, [obstacles[4], 600, 50, 50])
        score_text = font.render(f'Score: {score}', True, white, (0,0,0))
        display.blit(score_text, (1, 1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not active:
                if event.key == pygame.K_SPACE:
                    active = True
                    score = 0
                    player_x = 50
                    obstacles = [
    random.randint(600, 800), 
    random.randint(1000, 1200), 
    random.randint(1400, 1600), 
    random.randint(1800, 2000),
    random.randint(2200, 2400)
    ]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and y_change == 0:
                    y_change = 26
                if event.key == pygame.K_RIGHT:
                    x_change = 6
                if event.key == pygame.K_LEFT:
                    x_change = -6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = 0

        for i in range(len(obstacles)):
            if active:
                obstacles[i] -=obstacles_speed
                if obstacles[i] < -30:
                    obstacles[i] = random.randint(1200, 1800)
                    score += 15 
                    # if obstacles1.colliderect(obstacles0) or obstacles1.colliderect(obstacles2):
                    #     obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                    # if obstacles2.colliderect(obstacles0) or obstacles2.colliderect(obstacles1):
                    #     obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                    # if obstacles0.colliderect(obstacles1) or obstacles2.colliderect(obstacles2):
                    #     obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                    # if obstacles3.colliderect(obstacles2) or obstacles2.colliderect(obstacles1):
                    #     obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                    # if obstacles4.colliderect(obstacles1) or obstacles2.colliderect(obstacles2):
                    #     obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2) or player.colliderect(obstacles3) or player.colliderect(obstacles4):
                    active = False

        if 0 <= player_x <= monitor_size[0]:
            player_x += x_change
        if player_x < 0:
            player_x = 0
        if player_x > monitor_size[0]:  
            player_x = 430

        if y_change > 0 or player_y < 600:
            player_y -= y_change
            y_change -= gravity
        if player_y > 600:
            player_y = 600
        if player_y == 600 and y_change < 0:
            y_change = 0

        if score > 150:
            obstacles_speed = 7
        if score > 300:
            obstacles_speed = 8
        if score > 600:
            obstacles_speed = 9

        if active == False:
            display.fill(background)
            result_text = font.render(f'Score final: {score}', True, white, (0,0,0))
            instfim_text = font.render(f'Aperte espaço para fechar o jogo', True, white, (0,0,0))
            display.blit(result_text, (150, 120))
            display.blit(instfim_text, (70, 140))
            running = False
            handle_choose_name(score, 'infinity_runner')

        pygame.display.flip()

def menu():
    games = [
        "INFINITY RUNNER",
        "TETRIS"
    ]

    game_text_colors = [
        (240, 253, 244),
        (41, 55, 91, 1.0)
    ]

    game_cont = 0

    last_blink_time = pygame.time.get_ticks()
    show_text = True
    blink_interval = 300

    while True:
        color = game_text_colors[0] if show_text else game_text_colors[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if game_cont != 2:
                        game_cont += 1
                if event.key == pygame.K_UP:
                    if game_cont != 0:
                        game_cont -= 1
                if event.key == pygame.K_RETURN:
                    if game_cont == 0:
                        infinity_runner()
                    elif game_cont == 1:
                        battery_tetris()

        current_time = pygame.time.get_ticks()
        if current_time - last_blink_time > blink_interval:
            show_text = not show_text
            last_blink_time = current_time

        screen.fill((104, 203, 134, 1.0))

        main_menu_text = font.render("MENU PRINCIPAL", True, (41, 55, 91, 1.0))
        main_menu_text_rect = main_menu_text.get_rect(
            center=(monitor_size[0] // 2, 200))

        infinity_runner_text = font_sm.render(
            games[0], True, color if game_cont == 0 else (240, 253, 244))
        infinity_runner_text_rect = infinity_runner_text.get_rect(
            center=((monitor_size[0] // 2), (monitor_size[1] // 2) - 100))

        tetris_text = font_sm.render(
            games[1], True, color if game_cont == 1 else (240, 253, 244))
        tetris_text_rect = tetris_text.get_rect(
            center=((monitor_size[0] // 2), (monitor_size[1] // 2) + 300))

        screen.blit(main_menu_text, main_menu_text_rect)
        screen.blit(infinity_runner_text, infinity_runner_text_rect)
        screen.blit(tetris_text, tetris_text_rect)

        pygame.display.flip()

menu()
