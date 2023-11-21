import pygame
import sys
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

info = pygame.display.Info()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

screen = pygame.display.set_mode((monitor_size), pygame.RESIZABLE)
font = pygame.font.Font('retro.ttf', 124)
font_sm = pygame.font.Font('retro.ttf', 80)
clock = pygame.time.Clock()

def choose_name(score, game_name):
  alphabet = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
      'Y', 'Z'
  ]

  name = ['A', 'A', 'A']

  cont = 0
  letter = 0
  position = 0

  colors = [
  (22, 163, 74),
  (240, 253, 244)
  ]

  blink_interval = 500 
  last_blink_time = pygame.time.get_ticks()
  show_text = True

  while True: 
      color = colors[0] if show_text else colors[1]
      # Lidar com eventos
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_UP:
                  if cont == 0:
                      cont = 25
                  else:
                      cont -= 1
                      name[letter] = alphabet[cont]
              if event.key == pygame.K_DOWN:
                  if cont == 25:
                      cont = 0
                  else:
                      cont += 1

                  name[letter] = alphabet[cont]
              if event.key == pygame.K_RETURN:
                  if letter != 2:
                      letter += 1
                      position += 1
                  else:
                      score_csv = open(f'{game_name}.csv', 'a+')
                      score_csv.write(f'{"".join(name)}, {score}\n')
                      score_csv.close()
                      pygame.quit()
              
      # Letra piscando
      current_time = pygame.time.get_ticks()
      if current_time - last_blink_time > blink_interval:
          show_text = not show_text
          last_blink_time = current_time
          
      # Desenhando a tela
      screen.fill((5, 46, 22))

      # Definindo o que vai ser escrito
      name_text_blinking = font.render(f"{name[letter]}", True,  color)
      name_text = font.render(f"{''.join(name)}", True,  (240, 253, 244))
      text_rect = name_text.get_rect(center=(monitor_size[0] // 2, monitor_size[1] // 2))

      # Posição da letra que pisca
      blinking_letter_positions = [
          ((text_rect[0]), (text_rect[1])),
          ((text_rect[0]) + 96, (text_rect[1])),
          ((text_rect[0]) + (2 * 96), (text_rect[1])),
      ]

      # Escrevendo o texto 
      screen.blit(name_text, text_rect)
      screen.blit(name_text_blinking, blinking_letter_positions[position])
      
      # Update the display
      pygame.display.flip()
      
      # Limit the frame rate
      clock.tick(60)

def infinity_runner():
  white = (255, 255, 255)
  blue = (0, 0, 255)
  orange = (255, 165, 0)
  yellow = (255, 255, 0)

  display = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
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
  obstacles = [
      monitor_size[0] - random.randint(500, 1500), 
      monitor_size[0] - random.randint(500, 1500), 
      monitor_size[0] - random.randint(500, 1500), 
      monitor_size[0] - random.randint(500, 1500), 
      monitor_size[0] - random.randint(500, 1500)
    ]
  obstacles_speed = 3
  active = True
  score = 0

  running = True
  while running:
      timer.tick(fps)
      display.fill(background)
      floor = pygame.draw.rect(display, white, [0, 220, monitor_size[0], 5])
      player = pygame.draw.rect(display, (255,0,0), [player_x, player_y, 20, 20])
      obstacles0 = pygame.draw.rect(display, blue, [obstacles[0], 200, 20, 20])
      obstacles1 = pygame.draw.rect(display, orange, [obstacles[1], 200, 20, 20])
      obstacles2 = pygame.draw.rect(display, yellow, [obstacles[2], 200, 20, 20])
      obstacles3 = pygame.draw.rect(display, blue, [obstacles[2], 200, 20, 20])
      obstacles4 = pygame.draw.rect(display, orange, [obstacles[2], 200, 20, 20])
      score_text = font.render(f'Score: {score}', True, white, (0,0,0))
      display.blit(score_text, (1, 1))

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE and y_change == 0:
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
                  obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                  score += 1
                  if obstacles1.colliderect(obstacles0) or obstacles1.colliderect(obstacles2):
                    obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                  if obstacles2.colliderect(obstacles0) or obstacles2.colliderect(obstacles1):
                    obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                  if obstacles0.colliderect(obstacles1) or obstacles2.colliderect(obstacles2):
                    obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                  if obstacles3.colliderect(obstacles2) or obstacles2.colliderect(obstacles1):
                    obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
                  if obstacles4.colliderect(obstacles1) or obstacles2.colliderect(obstacles2):
                    obstacles[i] = random.randint(monitor_size[0], monitor_size[0])
              if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2):
                  active = False

      if 0 <= player_x <= monitor_size[0]:
          player_x += x_change
      if player_x < 0:
          player_x = 0
      if player_x > monitor_size[0]:
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
          running = False
          choose_name(score, 'infinity_runner')

      pygame.display.flip()

def menu():
    games = [
        "INFINITY RUNNER", 
        "SPACE INVADERS",
        "TETRIS"
    ]

    game_text_colors = [
        (240, 253, 244),
        (41,55,91,1.0)
    ]

    game_cont = 0

    last_blink_time = pygame.time.get_ticks()
    show_text = True
    blink_interval = 500 
    
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

        current_time = pygame.time.get_ticks()
        if current_time - last_blink_time > blink_interval:
            show_text = not show_text
            last_blink_time = current_time

        screen.fill((104,203,134,1.0))

        main_menu_text = font.render("MENU PRINCIPAL", True, (41,55,91,1.0))
        main_menu_text_rect = main_menu_text.get_rect(center=(monitor_size[0] // 2, 200))

        infinity_runner_text = font_sm.render(games[0], True, color if game_cont == 0 else (240, 253, 244))
        infinity_runner_text_rect = infinity_runner_text.get_rect(center=((monitor_size[0] // 2), (monitor_size[1] // 2) - 100))

        space_invaders_text = font_sm.render(games[1], True, color if game_cont == 1 else (240, 253, 244))
        space_invaders_text_rect = space_invaders_text.get_rect(center=((monitor_size[0] // 2), (monitor_size[1] // 2) + 100))

        tetris_text = font_sm.render(games[2], True, color if game_cont == 2 else (240, 253, 244))
        tetris_text_rect = tetris_text.get_rect(center=((monitor_size[0] // 2), (monitor_size[1] // 2) + 300))


        screen.blit(main_menu_text, main_menu_text_rect)
        screen.blit(infinity_runner_text, infinity_runner_text_rect)
        screen.blit(space_invaders_text, space_invaders_text_rect)
        screen.blit(tetris_text, tetris_text_rect)

        pygame.display.flip()

menu()
 