class GameState():
    def __init__(self):
        # if there is '!' at the end of the number it means it is inmutable, it came with start of the game
        self.board = [
            ["--", "--", "7!", "--", "1!", "--", "--", "--", "5!"],
            ["--", "--", "--", "2!", "--", "--", "--", "--", "--"],
            ["5!", "--", "1!", "9!", "8!", "4!", "--", "7!", "--"],
            ["4!", "--", "--", "--", "3!", "--", "7!", "--", "1!"],
            ["--", "1!", "8!", "7!", "--", "5!", "6!", "9!", "--"],
            ["7!", "5!", "--", "--", "--", "--", "--", "--", "--"],          
            ["9!", "6!", "2!", "--", "7!", "8!", "--", "1!", "--"],
            ["--", "--", "5!", "4!", "--", "9!", "3!", "--", "--"],
            ["3!", "--", "4!", "--", "6!", "1!", "8!", "--", "9!"]
        ]
        self.move_log = []

    def make_move(self, move):
        if self.board[move.squere_row][move.squere_col][1] != '!':
            if move.number == '0':
                self.board[move.squere_row][move.squere_col] = '--'
            else:
                self.board[move.squere_row][move.squere_col] = move.number + '-'
    
    def valid_move(self, move):
        moves = []
        # flag to check if same number is already on same row and col
        is_on_board = False
        directions = [(-1, 0), (1, 0), (0,-1), (0,1)]
        for d in directions:
            for i in range(1, 9):
                tmp_move_row = move.squere_row + d[0]*i
                tmp_move_col = move.squere_col + d[1]*i
                if 0 <= tmp_move_row <= 8 and 0 <= tmp_move_col <= 8: # on board
                    if self.board[tmp_move_row][tmp_move_col][0] == move.number:
                        is_on_board = True
                        break
        # check in "big squere"
        # IN PROGRESS
        
        if is_on_board:
            return False
        return True

class Move():
    def __init__(self, squere, board, number):
        self.squere_row = squere[0]
        self.squere_col = squere[1]
        self.number = str(number)
