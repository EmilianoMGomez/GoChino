import pygame
import math
import random
import numpy as np

# Define constantes para el juego
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BOARD_SIZE = 19
GRID_SIZE = 32
BOARD_WIDTH = GRID_SIZE * BOARD_SIZE
BOARD_HEIGHT = GRID_SIZE * BOARD_SIZE
WINDOW_WIDTH = BOARD_WIDTH + 200
WINDOW_HEIGHT = BOARD_HEIGHT
FPS = 30

# Inicializa Pygame y crea la ventana del juego
pygame.init()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Go Chinese")
clock = pygame.time.Clock()

# Carga las imágenes de las piedras
black_stone_img = pygame.image.load("black_stone.png").convert_alpha()
white_stone_img = pygame.image.load("white_stone.png").convert_alpha()

# Crea el tablero de juego
board = [[None for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

# Define la función para dibujar el tablero de Go
def draw_board():
    game_display.fill(GRAY)
    for i in range(BOARD_SIZE):
        x1 = GRID_SIZE + i * GRID_SIZE
        y1 = GRID_SIZE
        x2 = GRID_SIZE + i * GRID_SIZE
        y2 = BOARD_HEIGHT - GRID_SIZE
        pygame.draw.line(game_display, BLACK, (x1, y1), (x2, y2), 2)
        x1 = GRID_SIZE
        y1 = GRID_SIZE + i * GRID_SIZE
        x2 = BOARD_WIDTH - GRID_SIZE
        y2 = GRID_SIZE + i * GRID_SIZE
        pygame.draw.line(game_display, BLACK, (x1, y1), (x2, y2), 2)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            x = GRID_SIZE + i * GRID_SIZE
            y = GRID_SIZE + j * GRID_SIZE
            if board[i][j] == "black":
                game_display.blit(black_stone_img, (x-GRID_SIZE//2, y-GRID_SIZE//2))
            elif board[i][j] == "white":
                game_display.blit(white_stone_img, (x-GRID_SIZE//2, y-GRID_SIZE//2))

# Define la función para colocar una piedra en el tablero de Go
def place_stone(x, y, color):
    i = math.floor((x - GRID_SIZE / 2) / GRID_SIZE)
    j = math.floor((y - GRID_SIZE / 2) / GRID_SIZE)
    if i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
        return False
    if board[i][j] is None:
        board[i][j] = color
        return True
    else:
        return False

# Define la función para verificar si una piedra tiene libertades
def has_liberties(i, j, checked):
    if i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE:
        return False
    if (i, j) in checked:
        return False
    if board[i][j] is None:
        return True
    checked.append((i, j))
    if i > 0 and board[i][j] == board[i-1][j] and has_liberties(i-1, j, checked):
        return True
        if i < BOARD_SIZE-1 and board[i][j] == board[i+1][j] and has_liberties(i+1, j, checked):
         return True
    if j > 0 and board[i][j] == board[i][j-1] and has_liberties(i, j-1, checked):
        return True
    if j < BOARD_SIZE-1 and board[i][j] == board[i][j+1] and has_liberties(i, j+1, checked):
        return True
    return False

# Define la función para eliminar piedras sin libertades
def remove_dead_stones(color):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == color:
                if not has_liberties(i, j, []):
                    board[i][j] = None

# Define la función para contar el número de piedras de cada color en el tablero
def count_stones():
    black_count = 0
    white_count = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == "black":
                black_count += 1
            elif board[i][j] == "white":
                white_count += 1
    return (black_count, white_count)

# Define la función para determinar el color del jugador siguiente
def next_player(current_player):
    if current_player == "black":
        return "white"
    else:
        return "black"

# Define la función principal del juego
def play_game():
    current_player = "black"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_player == "black":
                    stone_img = black_stone_img
                else:
                    stone_img = white_stone_img
                mouse_x, mouse_y = event.pos
                if place_stone(mouse_x, mouse_y, current_player):
                    remove_dead_stones(next_player(current_player))
                    current_player = next_player(current_player)
        draw_board()
        black_count, white_count = count_stones()
        font = pygame.font.SysFont("Arial", 24)
        black_text = font.render("Black: {}".format(black_count), True, BLACK)
        white_text = font.render("White: {}".format(white_count), True, BLACK)
        game_display.blit(black_text, (BOARD_WIDTH+20, 20))
        game_display.blit(white_text, (BOARD_WIDTH+20, 60))
        pygame.display.update()
        clock.tick(FPS)
        
        # Función para realizar una jugada
        """
def make_move(x, y):
    global current_player
    if is_valid_move(x, y):
        board[x][y] = current_player
        if current_player == BLACK:
            current_player = WHITE
        else:
            current_player = BLACK
   """
        
        

# Inicia el juego
play_game()

