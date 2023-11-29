# Importa as bibliotecas necessárias
import pygame
import sys
from game import Game
from colors import Colors
from variables import MENU_PATH, TETRIS_PATH

# Adiciona o caminho do menu ao path do sistema
sys.path.append(f'{MENU_PATH}')

# Importa a função handle_choose_name do módulo choose_name
from choose_name import handle_choose_name

# Função principal que inicia o jogo Tetris
def battery_tetris():
    pygame.init()

    # Obtém o tamanho do monitor
    info = pygame.display.Info()
    monitor_size = [pygame.display.Info().current_w,
                    pygame.display.Info().current_h]

    # Configuração da fonte do título
    title_font = pygame.font.Font(None, 40)

    # Superfície de texto para exibir "GAME OVER"
    game_over_surface = title_font.render("GAME OVER", True, Colors.white)

    # Retângulo para exibir a pontuação
    score_rect = pygame.Rect(340, 50, 170, 60)

    # Retângulo para exibir a próxima peça
    next_rect = pygame.Rect(340, 255, 170, 180)

    # Configuração da janela do Pygame
    screen = pygame.display.set_mode(monitor_size, pygame.RESIZABLE)
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    # Criação do objeto do jogo
    game = Game()

    # Define um evento personalizado para atualização do jogo
    GAME_UPDATE = pygame.USEREVENT

    # Define a velocidade de queda das peças
    pygame.time.set_timer(GAME_UPDATE, 200)

    # Carrega e redimensiona a imagem de fundo
    background_image = pygame.image.load(f"{TETRIS_PATH}/fundo_tetris_pe.jpg")
    background_image = pygame.transform.scale(background_image, monitor_size)

    while True:
        # Loop principal do jogo
        for event in pygame.event.get():
            # Trata eventos do teclado e de encerramento do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Trata eventos de teclas pressionadas
                if game.game_over == True:
                    # Chama a função para lidar com a entrada do nome do jogador
                    return handle_choose_name(game.get_score(), 'tetris')
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
                # Atualiza a posição das peças com o evento personalizado
                game.move_down()

        # Desenha os elementos na tela
        score_value_surface = title_font.render(
            str(game.score), True, Colors.white)

        # Aplica a imagem de fundo
        screen.blit(background_image, background_image.get_rect())

        # Desenha o retângulo da pontuação
        pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                      centery=score_rect.centery))
        
        # Desenha o retângulo da próxima peça e as peças na tela
        pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
        game.draw(screen)

        # Atualiza a tela e controla a taxa de quadros
        pygame.display.update()
        clock.tick(60)

# Chama a função principal para iniciar o jogo Tetris
battery_tetris()
