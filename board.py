class Board:
    
    def __init__(self):
        # Initialize the board with the starting positions of the pieces
        
        self.turn = 'W'
        
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"],
        ]

    def __str__(self):
        # Generate a string representation of the board
        s = ""
        for i in range(8):
            for j in range(8):
                s += self.board[i][j]
            s += "\n"
        return s
