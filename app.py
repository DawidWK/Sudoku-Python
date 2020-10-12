import pygame
import sudokuEngine

#screen
WIDTH = HEIGHT = 504
DIMENSION = 9
SQUERE_SIZE = int(WIDTH/9)
BIG_SQUERE_SIZE = int(WIDTH/3)

'''
centers numbers in rectangle
'''
FIXED_ROW = 11
FIXED_COL = 18

'''
draws board only
'''
def draw_board(screen):    
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            pygame.draw.rect(screen, pygame.Color('grey'), pygame.Rect(column * SQUERE_SIZE,row * SQUERE_SIZE, SQUERE_SIZE, SQUERE_SIZE), 1)
    for row in range(3):
        for column in range(3):
            pygame.draw.rect(screen, pygame.Color('black'), pygame.Rect(column * BIG_SQUERE_SIZE,row * BIG_SQUERE_SIZE, BIG_SQUERE_SIZE, BIG_SQUERE_SIZE), 2)

'''
draws numbers from gameState
'''
def draw_numbers(screen, board, game_font):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(game_font.render(board[row][column][0], True, pygame.Color('black')), pygame.Rect(column * SQUERE_SIZE + FIXED_COL, row * SQUERE_SIZE + FIXED_ROW, SQUERE_SIZE, SQUERE_SIZE))

'''
checks if selected square is inmutable (is created with board)
'''
def check_if_inmutable(squere_selected, board):
    if squere_selected != ():
        if board[squere_selected[0]][squere_selected[1]][1] != '!':
            return True
    return False

'''
unchecks previous selected squere
'''
def uncheck_previous(selected, screen): 
    if len(selected) >= 1:
        s = pygame.Surface((SQUERE_SIZE, SQUERE_SIZE))
        row, col = selected[0]
        s.set_alpha(255) # transparency if 0 = completly transparent max = 255
        s.fill(pygame.Color('white'))
        screen.blit(s, (col*SQUERE_SIZE, row*SQUERE_SIZE))

'''
selects squere 
'''
def select_squere(selected, squere_selected, board):
    if check_if_inmutable(squere_selected, board):
        selected.append(squere_selected)
        print(selected)
    if len(selected) > 1:
        selected.pop(0)
    return selected[-1]

'''
highlights selected squere
'''
def highlight_squere(screen, selected, squere_selected, board):
    uncheck_previous(selected, screen)
    selected_now = select_squere(selected, squere_selected, board)
    s = pygame.Surface((SQUERE_SIZE, SQUERE_SIZE))
    row, col = selected_now
    s.set_alpha(100) # transparency if 0 = completly transparent max = 255
    s.fill(pygame.Color('blue'))
    screen.blit(s, (col*SQUERE_SIZE, row*SQUERE_SIZE))

def main():
    running = True
    pygame.init()
    gs = sudokuEngine.GameState()
    selected = []
    squere_selected = ()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_font = pygame.font.SysFont('dejavusans', 55)
    screen.fill(pygame.Color('white'))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # location of mouse 
                col = location[0]//SQUERE_SIZE
                row = location[1]//SQUERE_SIZE
                squere_selected = (row, col)
                highlight_squere(screen, selected, squere_selected, gs.board)
            if event.type == pygame.KEYDOWN and squere_selected != ():
                if event.key == pygame.K_0:
                    move = sudokuEngine.Move(squere_selected, gs.board, 0)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_1:
                    move = sudokuEngine.Move(squere_selected, gs.board, 1)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_2:
                    move = sudokuEngine.Move(squere_selected, gs.board, 2)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_3:
                    move = sudokuEngine.Move(squere_selected, gs.board, 3)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_4:
                    move = sudokuEngine.Move(squere_selected, gs.board, 4)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_5:
                    move = sudokuEngine.Move(squere_selected, gs.board, 5)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_6:
                    move = sudokuEngine.Move(squere_selected, gs.board, 6)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_7:
                    move = sudokuEngine.Move(squere_selected, gs.board, 7)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_8:
                    move = sudokuEngine.Move(squere_selected, gs.board, 8)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)
                if event.key == pygame.K_9:
                    move = sudokuEngine.Move(squere_selected, gs.board, 9)
                    gs.make_move(move)
                    highlight_squere(screen, selected, squere_selected, gs.board)

        draw_numbers(screen, gs.board, game_font)
        draw_board(screen)
        pygame.display.flip()
 

if __name__ == "__main__":
    main()
