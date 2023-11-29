# Importa as classes necessárias
from grid import Grid
from blocks import *
import random
import pygame
from variables import SOUNDS_PATH

# Classe que representa o estado do jogo Tetris
class Game:
    def __init__(self):
        # Inicializa as propriedades do jogo
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                       SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

        # Carrega os sons do jogo
        self.rotate_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound(f"{SOUNDS_PATH}/clear.ogg")
        
        self.game_over_time = 0

        # Configura a música de fundo
        pygame.mixer.music.load(f"{SOUNDS_PATH}/music.ogg")
        pygame.mixer.music.play(-1)

    # Atualiza a pontuação com base nas linhas limpas e nos pontos de movimento para baixo
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    # Retorna a pontuação atual
    def get_score(self):
        return self.score

    # Obtém um bloco aleatório da lista de blocos disponíveis
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                           SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Move o bloco para a esquerda
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    # Move o bloco para a direita
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    # Move o bloco para baixo
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # "Trava" o bloco no lugar, adicionando suas posições ao grid
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    # Reinicia o jogo
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(),
                       SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    # Verifica se o bloco cabe no grid
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    # Rotaciona o bloco
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    # Verifica se o bloco está dentro do grid
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # Desenha o estado atual do jogo na tela
    def draw(self, screen, width=535, height=80):
        self.grid.draw(screen, height + 400 // 2, width)
        # A mudança no x e y do grid.py precisa ser acompanhada da mesma mudança aqui
        self.current_block.draw(screen, height + 400 // 2, width)

        # Determina a posição do bloco seguinte com base no tipo de bloco
        if self.next_block.id == 3:
            self.next_block.draw(screen, 280, 290 + 40)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 280, 280 + 40)
        else:
            self.next_block.draw(screen, 290, 270 + 40)

    # Finaliza o jogo, aguardando um pequeno intervalo e encerrando o Pygame
    def over(self):
        pygame.time.delay(0)
        pygame.quit()
