from board import Board

def speech_to_text():
    pass

#returns the start and the finish of the move

    




curr_board = Board(8, 8)
print(curr_board.turn)

move = curr_board.get_input(curr_board, curr_board.turn)

#move the pieces and print
print(move)
# curr_board.display()

game_over = False

#start game
while not curr_board.winner:
    #get first user input
    curr_board.get_input(curr_board, curr_board.turn)

    #is checkmate?
    if curr_board.
    #switch turns 






curr_board.move([1, 1],[3,1], 'b')



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

