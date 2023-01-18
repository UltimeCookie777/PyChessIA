import piece

def replacePieces(boardEntity):
    
    board = boardEntity.board
    
    for y in range(len(board)):
        for x in range(len(board[y])):
            
            p = str(board[y][x])
            
            if p == " ":
                continue
            
            color = "black" if p.isupper() else "white"
            
            p = p.lower()

            if p == "p":
                p = piece.Pawn(color, [y, x])
            elif p == "r":
                p = piece.Rook(color, [y, x])
            elif p == "n":
                p = piece.Knight(color, [y, x])
            elif p == "b":
                p = piece.Bishop(color, [y, x])
            elif p == "q":
                p = piece.Queen(color, [y, x])
            elif p == "k":
                p = piece.King(color, [y, x])
                
            board[y][x] = p
    
    return board
            
def showMoves(boardEntity, moves):
    board = boardEntity.board
    
    showboard = str(board)
            
    return showboard
            
            

class Board:
    
    def __init__(self):
        # Initialize the board with the starting positions of the pieces
        
        self.turn = 'white'
        
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
            
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "],
            # [" ", " ", " ", " ", " ", " ", " ", " "]
        ]
        
    def removePiece(self, pos):
        
        y, x = pos
        
        self.board[y][x] = " "
        
    def placePiece(self, pos, piece):
        y, x = pos
        
        self.board[y][x] = piece
    
        
    def movePiece(self, pos, piece):
        self.removePiece(pos)
        self.placePiece(pos, piece)
        
        

    def __str__(self) -> str:
        # Generate a string representation of the board
        
        s = ""
        for i in range(8):
            for j in range(8):
                if str(self.board[i][j]) == " ":
                    s += "#"
                s += str(self.board[i][j])
            s += "\n"
        return s
