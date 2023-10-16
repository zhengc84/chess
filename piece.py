#pieces 

class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.pawn = False
        self.queen = False
        self.rook = False
        self.knight = False
        self.bishop = False 
        self.move_list = []

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)
    
    def change_pos(self, pos):
        self.row = pos[0] #x is stored in 0 
        self.col = pos[1] #y is stored in 1

    def __str__(self):
        return str(self.row) + " " + str(self.col)
    
class King(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.king = True
        self.name = 'k'

    def valid_moves(self, board):
        i = self.row
        j = self.col 

        moves = []

        #top left
        if i > 0:
            if j > 0:
                p = board[i-1][j-1]
                if p == 0:
                    moves.append((j - 1, i - 1))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1))

        #up 
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

        #top right
            if j < 7:
                p = board[i-1][j+1]
                if p == 0:
                    moves.append((j + 1, i - 1))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1))

        #bottom left
        if i < 7:
            if j > 0:
                p = board[i+1][j-1]
                if p == 0:
                    moves.append((j - 1, i + 1))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1))

            #bottom right
            if j < 7:
                p = board[i+1][j+1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))
            
            #down
            p == board[i+1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

        if j > 0:
            p = board[i][j-1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))
        
        if j < 7:
            p = board[i][j+1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))

        return moves


class Queen(Piece):
    
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.queen = True
        self.name = 'q'

    def valid_moves(self, board):
        #vertical and horizontal
        i = self.row 
        j = self.col
        
        moves = []
        
        #down
        for x in range(i - 1, -1 ,-1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #up
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #right 
        for y in range(j + 1, 8, 1):
            p = board[i][y]
            if p == 0:
                moves.append((y, i))
            elif p.color != self.color:
                moves.append((y, i))
                break
            else:
                break
        
        #left
        for y in range(j - 1, -1, -1):
            p = board[i][y]
            if p == 0:
                moves.append((y, i))
            elif p.color != self.color:
                moves.append((y, i))
                break
            else:
                break
        
        #diagonal
        djL = j + 1
        djR = j - 1

        #top right
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            
            djL += 1
        
        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            djR -= 1
        

        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            djL += 1

        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            djR -= 1
        
        return moves

class Pawn(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.pawn = True
        self.name = 'p'

    def valid_moves(self, board):
        #we need board because we need to check for other pieces
        i = self.row
        j = self.col

        moves = []
        try:
            #black
            if self.color == "b":
                if i < 7:
                    p = board[i+1][j]
                    if p == 0:
                        moves.append((j, i+1))
                    if j < 7:
                        p = board[i+1][j+1]
                        if p != 0 and p.color != self.color:
                            moves.append((j+1,i+1))
                    if j > 0:
                        p = board[i+1][j+1]
                        if p != 0 and p.color != self.color:
                            moves.append((j-1, i+1))
                
                if self.first == True:
                    if i < 6:
                        p = board[i+2][j]
                        if p == 0:
                            if board[i+1][j] == 0:
                                moves.append((j,i+2))
                        elif p.color != self.color:
                            moves.append((j+2, i))
            #White
            else:
                if i > 0:
                    p = board[i-1][j]
                    if p == 0:
                        moves.append((j,i-1))
                    if j < 7:
                        p = board[i-1][j+1]
                        if p != 0 and p.color != self.color:
                            moves.append((j+1,i-1))
                    if j > 0:
                        p = board[i-1][j-1]
                        if p != 0 and p.color != self.color:
                            moves.append((j-1, i-1))
                if self.first:
                    if i > 1: 
                        p = board[i-2][j]
                        if p == 0:
                            if board[i-1][j] == 0:
                                moves.append((j, i-2))
                        elif p.color != self.color:
                            moves.append((j, i-2))
        except:
            pass

        return moves


class Bishop(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.bishop = True
        self.name = 'b'

    def valid_moves(self, board):
         
        i = self.row 
        j = self.col 
        
        moves = []

        djL = j + 1
        djR = j - 1

        #top right
        for di in range(i - 1, -1, -1):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            
            djL += 1
        
        for di in range(i - 1, -1, -1):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            djR -= 1
        

        djL = j + 1
        djR = j - 1
        for di in range(i + 1, 8):
            if djL < 8:
                p = board[di][djL]
                if p == 0:
                    moves.append((djL, di))
                elif p.color != self.color:
                    moves.append((djL, di))
                    break
                else:
                    break
            djL += 1

        for di in range(i + 1, 8):
            if djR > -1:
                p = board[di][djR]
                if p == 0:
                    moves.append((djR, di))
                elif p.color != self.color:
                    moves.append((djR, di))
                    break
                else:
                    break
            djR -= 1
        
        return moves


class Knight(Piece):

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.knight = True
        self.name = 'n'

    def valid_moves(self, board):
        
        i = self.row
        j = self.col 

        moves = []

        #down left
        #down is increasing in row, 8 to 1 (most bottom row to top row)
        #left is from 1 to 8 

        if i < 6 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0:
                moves.append((j - 1, i + 2))
            elif p.color != self.color:
                moves.append((j - 1, i + 2))
            
        #up left
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))

        #center up left
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))
            elif p.color != self.color:
                moves.append((j + 1, i + 2))

        #center up right
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1, i - 2))

        #up right
        if i > 0 and j > 1:
            p = board[i - 1][j - 2]
            if p == 0:
                moves.append((i - 1, j - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))

        #down right
        if i > 0 and j < 6:
            p = board[i - 1][j - 2]
            if p == 0:
                moves.append((i - 1, j + 2))
            elif p.color != self.color:
                moves.append((i - 1, j + 2))

        #center down right
        if i < 7 and j < 6:
            p = board[i + 1][j + 2]
            if p == 0:
                moves.append((i + 1, j + 2))
            elif p.color != self.color:
                moves.append((i + 1, j + 2))

        #center down left
        if i < 7 and j > 1:
            p = board[i + 1][j - 2]
            if p == 0:
                moves.append((i + 1, j - 2))
            elif p.color != self.color:
                moves.append((i + 1, j - 2))

        return moves

class Rook(Piece):
    
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.rook = True
        self.name = 'r'

    def valid_moves(self, board):
        i = self.row 
        j = self.col
        
        moves = []
        
        #down
        for x in range(i - 1, -1 ,-1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #up
        for x in range(i + 1, 8, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break
        
        #right 
        for y in range(j + 1, 8, 1):
            p = board[i][y]
            if p == 0:
                moves.append((y, i))
            elif p.color != self.color:
                moves.append((y, i))
                break
            else:
                break
        
        #left
        for y in range(j - 1, -1, -1):
            p = board[i][y]
            if p == 0:
                moves.append((y, i))
            elif p.color != self.color:
                moves.append((y, i))
                break
            else:
                break
        
        return moves
