import pygame
import sys
from game import Game
from colors import Colors

MENU_PATH = r'C:/Users/acgs_cesar/Desktop/projetos 1/projeto-g12/src/menu'
TETRIS_PATH = r'C:/Users/acgs_cesar/Desktop/projetos 1/projeto-g12/src/tetris'

sys.path.append(f'{MENU_PATH}')
from choose_name import handle_choose_name


def battery_tetris():
    pygame.init()

    # Tamanho da tela
    info = pygame.display.Info()
    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]

    title_font = pygame.font.Font(None, 40)
    # Texto sobre next_rect
    # next_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)

    score_rect = pygame.Rect(340, 50, 170, 60)
    # Alterar next_block em game.py após alterar next_rect
    next_rect = pygame.Rect(340, 255, 170, 180)

    # DEFINE DISPLAY
    # Eixos x e y, respectivamente.
    screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    game = Game()

    GAME_UPDATE = pygame.USEREVENT

    # SET DA VELOCIDADE DE QUEDA
    pygame.time.set_timer(GAME_UPDATE, 200)

    # DEFINE BACKGROUND IMG
    background_image = pygame.image.load(f"{TETRIS_PATH}/fundo_tetris_pe.jpg")
    background_rect = background_image.get_rect()
    # REDIMENSIONA BACKGROUND IMG PARA O DISPLAY
    background_image = pygame.transform.scale(background_image, monitor_size)
    background_rect = background_image.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    handle_choose_name(game.get_score(), 'tetris')
                    game.over()
                    sys.exit()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        # Drawing
        score_value_surface = title_font.render(
            str(game.score), True, Colors.white)

        # APLICA A BACKGROUND IMG
        screen.blit(background_image, background_rect)
        # screen.fill(Colors.dark_blue)

        # screen.blit(score_surface, (365, 20, 50, 50))
        # screen.blit(next_surface, (375, 180, 50, 50))

        # if game.game_over == True:
        # screen.blit(game_over_surface, (320, 450, 50, 50))

        pygame.draw.rect(screen, Colors.laranja_avanade, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                      centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.laranja_avanade, next_rect, 0, 10)
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)
