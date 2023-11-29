from choose_name import handle_choose_name
import random
import os
import pygame
import sys
from variables import TETRIS_PATH, FONT_PATH
sys.path.append(TETRIS_PATH)
from main_tetris import battery_tetris


os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

info = pygame.display.Info()
monitor_size = [pygame.display.Info().current_w,
                pygame.display.Info().current_h]

screen = pygame.display.set_mode((monitor_size), pygame.RESIZABLE)
font = pygame.font.Font(FONT_PATH, 70)
font_sm = pygame.font.Font(FONT_PATH, 50)
clock = pygame.time.Clock()

def infinity_runner():
  # Definindo variáveis de cor
  white = (255, 255, 255)
  blue = (0, 0, 255)
  orange = (255, 165, 0)
  yellow = (255, 255, 0)
  purple = (128, 0, 128)
  green = (1, 50, 32)
  background = (0,0,0)

  # Comando para criar a janela do jogo e definir a sua resolução
  display = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
  pygame.display.set_caption('Infinite Runner')
  
  # Definindo a velocidade que o jogo vai rodar
  fps = 60
  # Definindo a fonte que o jogo irá usar
  font = pygame.font.Font(FONT_PATH, 20)
  # Comando que vai fazer o jogo rodar a velocidade definida anteriormente
  timer = pygame.time.Clock()

  # Definindo as posições iniciais do jogador
  player_x = 50
  player_y = 600

  # Variáveis de movimento do jogador
  y_change = 0
  x_change = 0
  # Variável que define a velocidade que o jogador cai
  gravity = 1.2
  
  # Definindo as posições iniciais dos obstáculos
  obstacles = [
    random.randint(600, 800), 
    random.randint(1000, 1200), 
    random.randint(1400, 1600), 
    random.randint(1800, 2000),
    random.randint(2200, 2400)
    ]
  
  # Definindo a velocidade inicial dos obstáculos
  obstacles_speed = 6

  # Variável que define o estado do jogo, desligado ou ligado
  active = True

  #Variável que armazena a pontuação do jogador
  score = 0

  # Outra variável de estado do jogo, para mostrar o menu no final
  running = True

  # Loop para deixar o jogo rodando até acabar
  while running:
        # Inicializa a velocidade do jogo pelo fps definido anteriormente
        timer.tick(fps)

        # Preenche o fundo do jogo 
        display.fill(background)

        # Desenha o chão do jogo
        floor = pygame.draw.rect(display, white, [0, 650, monitor_size[0], 10])

        # Desenha e posiciona o jogador no jogo
        player = pygame.draw.rect(display, (255,0,0), [player_x, player_y, 50, 50])

        # Desenha e posiciona os obstáculos no jogo
        obstacles0 = pygame.draw.rect(display, blue, [obstacles[0], 600, 50, 50])
        obstacles1 = pygame.draw.rect(display, orange, [obstacles[1], 600, 50, 50])
        obstacles2 = pygame.draw.rect(display, yellow, [obstacles[2], 600, 50, 50])
        obstacles3 = pygame.draw.rect(display, purple, [obstacles[3], 600, 50, 50])
        obstacles4 = pygame.draw.rect(display, green, [obstacles[4], 600, 50, 50])

        # Define o texto da pontuação
        score_text = font.render(f'Score: {score}', True, white, (0,0,0))
        # Mostra a pontuação na tela
        display.blit(score_text, (monitor_size[0]/2, 50))

        # Loop para captar todas as ações feitas no jogo
        for event in pygame.event.get():
            # Condição que finaliza o jogo se a janela for fechada
            if event.type == pygame.QUIT:
                running = False
            # Condição para quando o jogador apertar um botão
            if event.type == pygame.KEYDOWN:
                # Condição que faz o jogador pular se ele estiver no chão e apertar a seta para cima
                if event.key == pygame.K_UP and y_change == 0:
                    y_change = 28
                # Condição que faz o jogador ir para direita se ele segurar a seta para direita
                if event.key == pygame.K_RIGHT:
                    x_change = 6
                # Condição que faz o jogador ir para esquerda se ele segurar a seta para esquerda
                if event.key == pygame.K_LEFT:
                    x_change = -6
            # Condição para quando o jogador soltar um botão
            if event.type == pygame.KEYUP:
                # Condição para que o jogador para de ir para direita quando soltar a seta direita
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                # Condição para que o jogador para de ir para esquerda quando soltar a seta esquerda
                if event.key == pygame.K_LEFT:
                    x_change = 0

        # Loop para interagir com os obstáculos
        for i in range(len(obstacles)):
            if active:
                # Comando que faz os obstáculos irem para esquerda
                obstacles[i] -=obstacles_speed

                # Condição que faz o obstáculo voltar pra direita em uma posição aleatória se ele passar da tela
                if obstacles[i] < -30:
                    obstacles[i] = random.randint(1200, 1800)
                    score += 15 

                # Condição para terminar o jogo se o jogador entrar em contato com um obstáculo
                if player.colliderect(obstacles0) or player.colliderect(obstacles1) or player.colliderect(obstacles2) or player.colliderect(obstacles3) or player.colliderect(obstacles4):
                    active = False

        # Condição para o player receber a variável de movimento e se mover caso ela seja modificada
        if 0 <= player_x <= monitor_size[0]:
            player_x += x_change
        # Condição para o player não sair da parte direita da tela se ele chegar no limite dela
        if player_x < 0:
            player_x = 0
        # Condição para o player não sair da parte direita da tela se ele chegar no limite dela
        if player_x > monitor_size[0]:  
            player_x = monitor_size[0]

        # Condição para o player receber a variável de movimento e se mover caso ela seja modificada, além do jogador ser afetado por gravidade quando ele pula
        if y_change > 0 or player_y < 600:
            player_y -= y_change
            y_change -= gravity
        # Condição para o jogador voltar a altura do chão caso ele passe dela
        if player_y > 600:
            player_y = 600
        # Concição para o player parar de modificar a sua altura quando ele atinge o chão
        if player_y == 600 and y_change < 0:
            y_change = 0

        # Condições para os obstacúlos ficarem mais rápidos caso o jogador atinja uma certa quantidade de pontos
        if score > 150:
            obstacles_speed = 7
        if score > 300:
            obstacles_speed = 8
        if score > 600:
            obstacles_speed = 9

        # Condição para mostrar a pontuação quando o jogo acabar
        if active == False:
            running = False
            handle_choose_name(score, 'infinity_runner')
            return 0

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

    # resting_screen()

    conttador = 0
    while True:
        if conttador == 0:
            conttador = resting_screen()
        else:
            color = game_text_colors[0] if show_text else game_text_colors[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if game_cont != 1:
                            game_cont += 1
                        elif game_cont == 1:
                            game_cont = 0
                    if event.key == pygame.K_UP:
                        if game_cont != 0:
                            game_cont -= 1
                    
                    if event.key == pygame.K_RIGHT:
                        if game_cont == 0:
                            conttador = infinity_runner()
                        elif game_cont == 1:
                            conttador = battery_tetris()
                            game_cont = 0

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
                center=((monitor_size[0] // 2), (monitor_size[1] // 2) + 100))

            tetris_text = font_sm.render(
                games[1], True, color if game_cont == 1 else (240, 253, 244))
            tetris_text_rect = tetris_text.get_rect(
                center=((monitor_size[0] // 2), (monitor_size[1] // 2) + 300))

            screen.blit(main_menu_text, main_menu_text_rect)
            screen.blit(infinity_runner_text, infinity_runner_text_rect)
            screen.blit(tetris_text, tetris_text_rect)

            pygame.display.flip()

def resting_screen():    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #precisa resolver conflito
                    contador = 1
                    return contador
                
        background_image = pygame.image.load(r"C:\Users\acgs_cesar\Desktop\surto coletivo\projeto-g12\src\menu\assets\mascote.png")
        background_rect = background_image.get_rect()
        background_image = pygame.transform.scale(background_image, monitor_size)
        screen.blit(background_image, background_rect)
        pygame.display.flip()


# resting_screen()
menu()
                              