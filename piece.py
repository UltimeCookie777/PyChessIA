def squareExist(pos) -> list:
    # Unpack the row and column indices from the square tuple
    row, col = pos
    # Return True if the indices are both between 0 and 7 (inclusive), False otherwise
    
    if 0 <= row <= 7 and 0 <= col <= 7:
        return pos
    else:
        return [-1,-1]

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False
    
    def move(self, new_position):
        # Update the piece's position and has_moved attribute
        self.position = new_position
        self.has_moved = True
    
    def possible_moves(self):
        # Return a list of all the legal squares the piece could move to
        # Given the current state of the board
        pass
    
class Pawn(Piece):
    
    def __init__(self, color, position) -> None:
        
        super().__init__(color, position)
        
        self.value = 1
        self.color = color
        self.has_moved = False
        self.position = position
        
    def possible_moves(self):
        
        if self.color == "white":

            return [
                    squareExist([self.position[0] -1, self.position[1] +1]),
                    squareExist([self.position[0] +1, self.position[1] +1])
                    ]
        
        return [squareExist([self.position[0] -1, self.position[1] -1]), squareExist([self.position[0] +1, self.position[1]-1])]
    

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def possible_moves(self):
        return super().possible_moves()
    
class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def possible_moves(self):
        return super().possible_moves()
    
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def possible_moves(self):
        return super().possible_moves()
    
    
class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def possible_moves(self):
        return super().possible_moves()
    
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def possible_moves(self):
        return super().possible_moves()