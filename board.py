#keep board state - this is what should be checked with arduino info to confirm moves
from piece import Pawn
from piece import Rook 
from piece import King
from piece import Knight
from piece import Queen
from piece import Bishop
import time


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 

        self.board = [[0 for i in range(8)] for _ in range(8)]

        self.board[0][0] = Rook(0, 0, 'b') #H1
        self.board[0][1] = Knight(0, 1, 'b')
        self.board[0][2] = Bishop(0, 2, 'b')
        self.board[0][3] = Queen(0, 3, 'b')
        self.board[0][4] = King(0, 4, 'b')
        self.board[0][5] = Bishop(0, 5, 'b')
        self.board[0][6] = Knight(0, 6, 'b')
        self.board[0][7] = Rook(0, 7, 'b') #H8 
        self.board[1][0] = Pawn(1, 0, 'b')
        self.board[1][1] = Pawn(1, 1, 'b')
        self.board[1][2] = Pawn(1, 2, 'b')
        self.board[1][3] = Pawn(1, 3, 'b')
        self.board[1][4] = Pawn(1, 4, 'b')
        self.board[1][5] = Pawn(1, 5, 'b')
        self.board[1][6] = Pawn(1, 6, 'b')
        self.board[1][7] = Pawn(1, 7, 'b')

        #white
        self.board[7][0] = Rook(7, 0, 'w') #A1 
        self.board[7][1] = Knight(7, 1, 'w')
        self.board[7][2] = Bishop(7, 2, 'w')
        self.board[7][3] = Queen(7, 3, 'w')
        self.board[7][4] = King(7, 4, 'w')
        self.board[7][5] = Bishop(7, 5, 'w')
        self.board[7][6] = Knight(7, 6, 'w')
        self.board[7][7] = Rook(7, 7, 'w') #H1 
        self.board[6][0] = Pawn(6, 0, 'w')
        self.board[6][1] = Pawn(6, 1, 'w')
        self.board[6][2] = Pawn(6, 2, 'w')
        self.board[6][3] = Pawn(6, 3, 'w')
        self.board[6][4] = Pawn(6, 4, 'w')
        self.board[6][5] = Pawn(6, 5, 'w')
        self.board[6][6] = Pawn(6, 6, 'w')
        self.board[6][7] = Pawn(6, 7, 'w')

        self.turn = 'w'

        self.winner = None

        self.last = None 

        self.wTime = 900
        self.bTime=  900

        self.storedTime1 = 0
        self.storedTime2 = 0

        self.startTime = time.time()


    #get the valid moves of all pieces
    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)

    def display(self):
        boardstate = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    temp.append(' ')
                else:
                    temp.append(self.board[i][j].name)
            boardstate.append(temp)
        
        print(boardstate)
                

    def get_checked_moves(self, color):
        checked_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for moves in self.board[i][j].move_list:
                            checked_moves.append(moves)
        return checked_moves

    def checked(self, color):
        self.update_moves()
        checked_moves = self.get_checked_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i)
        
        
        
        if king_pos in checked_moves:
            return True
        
        return False

    def checkmate(self, color):
        if self.checked(color):
            king = None
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] != 0:
                        if self.board[i][j].king and self.board[i][j].color == color:
                            king = self.board[i][j]
            
            if king is not None:
                all_moves = king.valid_moves(self.board)
                danger_moves = self.get_checked_moves(self.color)
                
                danger_count = 0
                for moves in all_moves:
                    if move in danger_moves:
                        danger_count += 1 
                
                if danger_count == len(all_moves):
                    return True


        return False


    def get_input(self, board, color):
        self.update_moves()
        col_dict = {
         'a' : 0,
         'b' : 1,
         'c' : 2,
         'd' : 3,
         'e' : 4,
         'f' : 5,
         'g' : 6,
         'h' : 7
        }
        move = input('please enter a move: ')
        row = None
        col = None
        unit = None
        spec_row = None
        spec_col = None
        

        final_move = []

        
        #might have to add in some sort of input checking
        # 1. if the move is 2 characters long (pawn specific)
        if len(move) == 2:
            col = move[0].lower()
            row = move[1]

        # 2. if the move is 3 characters long (unit and move)
        elif len(move) == 3:
            unit = move[0].lower()
            col = move[1].lower()
            row = move[2]

        # 3. if the move is 4 characters long (unit + col + move)
        elif len(move) == 4:
            unit = move[0].lower()
            spec_row = move[1]
            col = move[1].lower()
            row = move[2]

        elif len(move) == 5:
            unit = move[0].lower()
            spec_col = move[1].lower()
            spec_row = move[2]
            col = move[3].lower()
            row = move[4]
        else:
            print("Invalid move")


        if col not in col_dict:
            print(col)
            return []
        else:
            col = col_dict[col]
            row = 8 - int(row)
        
        if spec_col:
            spec_col = int(spec_col)
        if spec_row:
            spec_row = int(spec_row)
        if unit == None:
            unit = 'p'

        #the return statement should return a start, and an end
        # return [unit, spec_col, spec_row, col, row]

        #specified it is pawn
        #if both are given, just check that space
        print(unit)
        print(col)
        print(row)
        print(spec_col)
        print(spec_row)
        
        if spec_col and spec_row:
            if self.board[spec_row][spec_col] != 0:
                if self.board[spec_row][spec_col].color == color:
                    if (col, row) in self.board[spec_row][spec_col].move_list:
                        final_move.append((spec_row, spec_col))
                        final_move.append((row, col))
        
        #if specific column is given, just check that column
        elif spec_col:
            for i in range(8):
                if self.board[i][spec_col] != 0: 
                    if self.board[i][spec_col].name == unit and self.board[i][spec_col] == color:
                        if (col, row) in self.board[i][spec_col].move_list:
                            final_move.append((i, spec_col))
                            final_move.append((row, col))


        elif spec_row:
            for i in range(8):
                if self.board[spec_row][i] != 0:
                    if self.board[spec_row][i].name == unit and self.board[spec_row][i].color == color:
                        if (col, row) in self.board[spec_row][i].move_list:
                            final_move.append((spec_row, i))
                            final_move.append((row, col))

        else:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] != 0:
                        if self.board[i][j].name == unit and self.board[i][j].color == color:
                            print(self.board[i][j].move_list)
                            if (col, row) in self.board[i][j].move_list:
                                final_move.append((i, j))
                                final_move.append((row, col))

                        
        if not final_move:
            print(final_move)
            return ('invalid move')
        else:
            print(final_move)
            return final_move

        
    def move(self, board, color):
        move_input = self.get_input(board, color)
        #have to make sure not in check or move out of check
        start = move_input[0]
        end = move_input[1]
        under_check = self.checked(color)
        cboard = self.board[:]
        changed = False
        
        #if the piece is a pawn
        if cboard[start[0]][start[1]].pawn:
            cboard[start[0]][start[1]].first = False
        
        cboard[start[0]][start[1]].change_pos((end[0],end[1]))
        cboard[end[0]][end[1]] = cboard[start[0]][start[1]]
        cboard[start[0]][start[1]] = 0
        self.board = cboard
        changed = True

        if self.checked(color) or (under_check and self.checked(color)):
            cboard = self.board[:]
            if cboard[end[0]][end[1]].pawn:
                cboard[end[0]][end[1]].first = True
            
            cboard[end[0]][end[1]].change_pos((start[0],start[1]))
            cboard[start[0]][start[1]] = cboard[end[0]][end[1]]
            self.board = cboard
            changed = False

        if changed:
            self.last = (start, end)
            if self.turn == "w":
                self.storedTime1 += (time.time() - self.startTime)
            else:
                self.storedTime2 += (time.time() - self.startTime)

        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'

        return changed


if __name__ == "__main__":
    curr_board = Board(8, 8)
    moved = False

    while not curr_board.winner:

        #print the current turn
        if curr_board.turn == 'w':
            print('turn: white')
        else:
            print('turn: black')

        # try:
        if curr_board.move(curr_board, curr_board.turn):
            print('true')
            curr_board.display()
        else:
            print("error")
        # except:
        #     print("unable to process")


# 8 [0, 0] [0, 1] [0, 2] [0, 3] [0, 4] [0, 5] [0, 6] [0, 7]
# 7 [1, 0] [1, 1] [1, 2] [1, 3] [1, 4] [1, 5] [1, 6] [1, 7]
# 6 [2, 0] [2, 1] [2, 2] [2, 3] [2, 4] [2, 5] [2, 6] [2, 7]
# 5 [3, 0] [3, 1] [3, 2] [3, 3] [3, 4] [3, 5] [3, 6] [3, 7]
# 4 [4, 0] [4, 1] [4, 2] [4, 3] [4, 4] [4, 5] [4, 6] [4, 7]
# 3 [5, 0] [5, 1] [5, 2] [5, 3] [5, 4] [5, 5] [5, 6] [5, 7]
# 2 [6, 0] [6, 1] [6, 2] [6, 3] [6, 4] [6, 5] [6, 6] [6, 7]
# 1 [7, 0] [7, 1] [7, 2] [7, 3] [7, 4] [7, 5] [7, 6] [7, 7]
#     A      B      C      D      E      F      G      H
#     0      1      2      3      4      5      6      7

                    




            