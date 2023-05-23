
#we need the board
import board

class Piece:
    def __init__(self, color, position, piece_type):
        self.color = color
        self.position = position
        self.piece_type = piece_type

class Pawn(Piece):
    def __init__(self, color, position, first_move):
        #color: True = white, false = black
        super().__init__(color,position, 'pawn')
        self.first_move = True

    def is_valid_moves(self, board, start, end):
        #update the list of valid moves? list of valid moves?
        #or pass in the move that it wants to go and move there
        #position is given in an array
        
        #first move
        if 
        
        #capture

        #promotion

        else:
            



class Rook(Piece):
    #todo: write the rook class
    def __init__(self, color, position):
        super().__init__(color,position, 'rook')


class Knight(Piece):
    #todo: write the rook class
    def __init__(self, color, position):
        super().__init__(color,position, 'knight')
    
class Bishop(Piece):
    #todo: write the rook class
    def __init__(self, color, position):
        super().__init__(color,position, 'bishop')

class King(Piece):
    #todo: write the rook class
    def __init__(self, color, position):
        super().__init__(color,position, 'king')

class Queen(Piece):
    #todo: write the rook class
    def __init__(self, color, position):
        super().__init__(color,position, 'queen')
    
