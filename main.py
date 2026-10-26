from src.chess_engine.board import Board

board = Board()
board.board = [["" for _ in range(8)] for _ in range(8)]
board.move_history = []
board.white_to_move = True

board.board[0][0] = "k"
board.board[0][4] = "r"
board.board[6][4] = "R"
board.board[7][4] = "K"

legal_moves = board.get_legal_moves()

pinned_move = any(
    move.start == (6, 4) and move.end == (6, 3)
    for move in legal_moves
)

blocking_move = any(
    move.start == (6, 4) and move.end == (5, 4)
    for move in legal_moves
)

print("Pinned sideways move:", pinned_move)
print("Move maintaining the block:", blocking_move)
print("Board restored:", board.board[6][4] == "R")
print("Turn restored:", board.white_to_move)
print("History empty:", len(board.move_history) == 0)