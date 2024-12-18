import array as arr

#The current board states
class BoardState:
    board = [[0 for i in range(8)] for i in range(8)] #board is initialized as all 0's
                                                      #numbers/enums will represent where pieces are
    whitesTurn = True #since game begins on whites turn, this is true by default
    def __init__(self, board, whitesTurn): #board: 8x8 array (2d), whitesTurn: boolean, return: object
        self.board = board
        self.whitesTurn = whitesTurn

    #To be implemented, determines if "move" is legal
    def isLegalMove(self, move): #move: string, return: boolean
        print("WIP")

#The chess engine itself is essentially a single function; it takes
#a board state (which comes with a specific players turn) as input
#and outputs the move the chess engine believes is best.
def ChessEngine(boardState): #boardState: BoardState, return: string
    print("WIP")


