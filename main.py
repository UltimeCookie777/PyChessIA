import board
import piece

def main():
    
    boardEntity = board.Board()

    boardEntity.board = board.replacePieces(boardEntity)

    # p = piece.Pawn("white", [6,1])

    # p2 = piece.Pawn("black", [4,3])

    # r = piece.Rook("black", [6,3])

    # boardEntity.placePiece(p.position, p)
    # boardEntity.placePiece(p2.position, p2)
    # boardEntity.placePiece(r.position, r)



    print(boardEntity)

    print(board.showMoves(boardEntity, boardEntity.board[0][0].possible_moves(boardEntity)))


if __name__ == "__main__":
    main()