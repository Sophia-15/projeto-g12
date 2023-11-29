# Importa a biblioteca Pygame e a classe Colors
import pygame
from colors import Colors

# Classe que representa o grid do jogo Tetris
class Grid:
    def __init__(self):
        # Inicializa as propriedades do grid
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Cria uma matriz para representar o grid, inicializada com zeros
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Obtém as cores das células do módulo Colors
        self.colors = Colors.get_cell_colors()

    # Método para imprimir o grid no console (usado para depuração)
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    # Verifica se uma posição (linha, coluna) está dentro dos limites do grid
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Verifica se uma célula específica está vazia
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # Verifica se uma linha está completamente preenchida
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # Limpa uma linha específica, definindo todas as suas células como vazias
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # Move uma linha para baixo, dado um número específico de linhas
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # Limpa as linhas completamente preenchidas e move as linhas acima para baixo
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # Reinicia o grid, definindo todas as células como vazias
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # Desenha o grid na tela do jogo usando Pygame
    def draw(self, screen, width, height):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Cria um retângulo para representar a célula na tela
                cell_rect = pygame.Rect(column * self.cell_size + width, row * self.cell_size + height,
                                        self.cell_size - 1, self.cell_size - 1)
                # Desenha o retângulo na tela usando a cor correspondente da paleta de cores
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
