from src.chess_engine.board import Board
from src.chess_engine.move import Move


board = Board()
board.create_board()
board.board[5][0] = "P"
board.board[5][0] = "p"
print(board.get_knight_moves(7,1))