from src.chess_engine.board import Board

# Test 1: White pawn from e2
board = Board()
print("White pawn e2:")
print(board.get_pawn_moves(6, 4))
# Expected: [(5, 4), (4, 4)]


# Test 2: Black pawn from e7
board = Board()
print("Black pawn e7:")
print(board.get_pawn_moves(1, 4))
# Expected: [(2, 4), (3, 4)]


# Test 3: Piece directly in front blocks pawn
board = Board()
board.board[5][4] = "n"   # put a black knight on e3
print("Blocked white pawn:")
print(board.get_pawn_moves(6, 4))
# Expected: []


# Test 4: White pawn can capture enemy diagonally
board = Board()
board.board[5][3] = "p"   # black pawn on d3
print("White pawn with enemy diagonal:")
print(board.get_pawn_moves(6, 4))
# Expected to include:
# (5, 4), (4, 4), (5, 3)


# Test 5: White pawn cannot capture friendly piece
board = Board()
board.board[5][3] = "P"   # white pawn on d3
print("White pawn with friendly diagonal:")
print(board.get_pawn_moves(6, 4))
# Expected:
# [(5, 4), (4, 4)]


# Test 6: Pawn on edge should not wrap around
board = Board()
board.board[6][0] = ""    # remove original a2 pawn
board.board[4][0] = "P"   # put white pawn on a4
board.board[3][7] = "p"   # enemy on h5 — must NOT be capturable
print("White pawn on a-file:")
print(board.get_pawn_moves(4, 0))
# Should NOT contain (3, 7)