from src.chess_engine.board import Board
from src.chess_engine.move import Move


board = Board()

move1 = Move((6, 4), (4, 4))  # e2 -> e4
board.make_move(move1)

move2 = Move((1, 3), (3, 3))  # d7 -> d5
board.make_move(move2)

move3 = Move((4, 4), (3, 3))  # e4 -> d5, capture
board.make_move(move3)

board.display()
board.undo_move()
board.display()