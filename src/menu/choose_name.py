import os
import pygame
import sys
from variables import FONT_PATH

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()

info = pygame.display.Info()
monitor_size = [pygame.display.Info().current_w,
                pygame.display.Info().current_h]

screen = pygame.display.set_mode((monitor_size), pygame.RESIZABLE)
font = pygame.font.Font(FONT_PATH, 124)
font_sm = pygame.font.Font(FONT_PATH, 80)
clock = pygame.time.Clock()

def handle_choose_name(score, game_name):
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

    blink_interval = 250
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
                if event.key == pygame.K_RIGHT:
                    if letter != 2:
                        letter += 1
                        position += 1
                        cont = 0
                    else:
                        score_csv = open(f'{game_name}.csv', 'a+')
                        score_csv.write(f'{"".join(name)}, {score}\n')
                        score_csv.close()
                        return 0
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
        text_rect = name_text.get_rect(
            center=(monitor_size[0] // 2, monitor_size[1] // 2))

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
