import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load chess pieces images
pieces = {
    'r': pygame.transform.scale(pygame.image.load('images/r.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'n': pygame.transform.scale(pygame.image.load('images/n.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'b': pygame.transform.scale(pygame.image.load('images/b.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'q': pygame.transform.scale(pygame.image.load('images/q.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'k': pygame.transform.scale(pygame.image.load('images/k.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'p': pygame.transform.scale(pygame.image.load('images/p.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'R': pygame.transform.scale(pygame.image.load('images/R.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'N': pygame.transform.scale(pygame.image.load('images/N.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'B': pygame.transform.scale(pygame.image.load('images/B.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'Q': pygame.transform.scale(pygame.image.load('images/Q.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'K': pygame.transform.scale(pygame.image.load('images/K.png'), (SQUARE_SIZE, SQUARE_SIZE)),
    'P': pygame.transform.scale(pygame.image.load('images/P.png'), (SQUARE_SIZE, SQUARE_SIZE)),
}

# Initialize the board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

selected_square = None
turn = 'white'

def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != '.':
                screen.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

def get_square(pos):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE

def move_piece(start, end):
    global turn
    piece = board[start[0]][start[1]]
    # Basic turn validation
    if (turn == 'white' and piece.isupper()) or (turn == 'black' and piece.islower()):
        board[end[0]][end[1]] = piece
        board[start[0]][start[1]] = '.'
        turn = 'black' if turn == 'white' else 'white'

def main():
    global selected_square
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_square(pos)
                if selected_square:
                    move_piece(selected_square, (row, col))
                    selected_square = None
                else:
                    selected_square = (row, col)

        screen.fill(BLACK)
        draw_board()
        pygame.display.flip()

if __name__ == "__main__":
    main()
