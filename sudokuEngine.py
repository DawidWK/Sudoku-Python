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

class Move():
    def __init__(self, squere, board, number):
        self.squere_row = squere[0]
        self.squere_col = squere[1]
        self.number = str(number)
