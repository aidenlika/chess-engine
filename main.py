from src.chess_engine.board import Board

board = Board()
board.board = [["" for _ in range(8)] for _ in range(8)]
board.move_history = []
board.white_to_move = False

board.board[0][7] = "k"
board.board[7][7] = "K"
board.board[6][0] = "p"

move = next(
    move for move in board.get_all_moves()
    if move.start == (6, 0) and move.end == (7, 0)
)

board.make_move(move)
print(board.board[7][0])  # q

board.undo_move()
print(board.board[6][0])  # p
print(board.white_to_move)  # False