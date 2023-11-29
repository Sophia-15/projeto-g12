# Importa as classes necessárias
from colors import Colors
import pygame
from position import Position

# Classe base que representa um bloco no jogo Tetris
class Block:
    def __init__(self, id):
        # Inicializa as propriedades do bloco
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    # Move o bloco por um número específico de linhas e colunas
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # Obtém as posições absolutas das células do bloco após o movimento
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # Rotaciona o bloco no sentido horário
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Desfaz a última rotação realizada
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # Desenha o bloco na tela com base nas posições das células
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
                                     offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
