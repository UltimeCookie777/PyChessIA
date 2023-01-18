def squareExist(pos) -> list:
    x, y = pos
    
    if 0 <= x <= 7 and 0 <= y <= 7:
        return pos
    else:
        return []

def removeInvalidSquares(List) -> list:
    while [-1,-1] in List:
        List.remove([-1,-1])
        
    while [] in List:
        List.remove([])
        
    return List

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False
        
    def __str__(self) -> str:
        return f"{self.color[0]}{self.__class__.__name__[0]}"
    
    def move(self, new_position):
        self.position = new_position
        self.has_moved = True
    
    def possible_moves(self):
        pass
    
class Pawn(Piece):
    
    def __init__(self, color, position) -> None:
        
        super().__init__(color, position)
        
        self.value = 1.0
        
    def __str__(self) -> str:
        return f"{self.color[0]}{self.__class__.__name__[0]}"
    
    def possible_moves(self, _):
        
        if self.color == "white":

            moves = [
                    squareExist([self.position[0] +1, self.position[1] -1]),
                    squareExist([self.position[0] +1, self.position[1] +1])
                    ]
        else:
            
            moves = [squareExist([self.position[0] -1, self.position[1] +1]),
                     squareExist([self.position[0] -1, self.position[1]-1])]

        return removeInvalidSquares(moves)
    

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.value = 5.1
        
        
    # I have no idea how or why it works and i'm afraid to touch it
    def possible_moves(self, boardEntity) -> list:
        moves = []
        
        for plusx in range(1, 8-int(self.position[1])):

            case = boardEntity.board[self.position[0]][self.position[1] + plusx]

            if case.__str__() == " ":
                moves.append(squareExist([self.position[0], self.position[1] + plusx]))
                continue
            
            if not case.color == self.color:
                moves.append(squareExist([self.position[0], self.position[1] + plusx]))
                break
            else:
                break
        
        
  
        for minusx in range(1, int(self.position[1]) + 1):
            
            case = boardEntity.board[self.position[0]][self.position[1]  - minusx]
            
            if case.__str__() == " ":
                moves.append(squareExist([self.position[0], self.position[1] - minusx]))
                continue
            
            if not case.color == self.color:
                moves.append(squareExist([self.position[0], self.position[1] - minusx]))
                break
            else:
                break
         
        for plusy in range(1, int(self.position[0]) + 1):
            
            case = boardEntity.board[self.position[0] - plusy][self.position[1]]
            
            if str(case) == " ":
                moves.append(squareExist([self.position[0] - plusy, self.position[1]]))
                continue
            
            if not case.color == self.color:
                moves.append(squareExist([self.position[0] - plusy, self.position[1]]))
                break
            else:
                break
            
        for minusy in range(1, 8 - int(self.position[0])):
            
            case = boardEntity.board[self.position[0] + minusy][self.position[1]]
        
            if str(case) == " ":
                moves.append(squareExist([self.position[0] + minusy, self.position[1]]))
                continue
            
            if not case.color == self.color:
                moves.append(squareExist([self.position[0] + minusy, self.position[1]]))
                break
            else:
                break
            
        return removeInvalidSquares(moves)
           
            
        
          
            
        













class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.value = 3.2
        
    def possible_moves(self):
        return super().possible_moves()
    
class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.value = 3.3
    
    def possible_moves(self) -> list:
        return []
    
    
class Queen(Bishop, Rook):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.value = 8.8
       
    def possible_moves(self):
        return super(Bishop).possible_moves() + super(Rook).possible_moves() # type: ignore
     
class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def possible_moves(self):
        return super().possible_moves()