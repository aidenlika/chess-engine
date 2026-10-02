from src.chess_engine.board import Board
from src.chess_engine.move import Move


board = Board()
board.board[1][7] = ""
print(board.get_rook_moves(0,7))