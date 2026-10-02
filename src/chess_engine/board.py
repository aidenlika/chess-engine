class Board:
    def __init__(self):
        self.board = self.create_board()
        self.move_history = []

    def create_board(self):

        board = [["" for _ in range(8)] for _ in range(8)] # Initialise empty 8x8 board

        board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # White pieces
        board[6] = ['P'] * 8  # White pawns
        board[1] = ['p'] * 8  # Black pawns
        board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']  # Black pieces
        
        return board

    
    def display(self):
        displayed = []
        for row in self.board:
            displayed_row = []
            for c in range(8):
                if row[c] == "":
                    displayed_row.append(".")
                else:
                    displayed_row.append(row[c])
            displayed.append(displayed_row)
                
        for k in displayed:
            print(" ".join(k))

    def make_move(self, move):
        to_be_moved_row,to_be_moved_column = move.start # Unpack tuples of original piece position
        start_piece = self.board[to_be_moved_row][to_be_moved_column]
       
        
        new_pos_row,new_pos_column = move.end   # Unpack tuples of position to move piece to
        destination_piece = self.board[new_pos_row][new_pos_column]
        self.move_history.append((move,start_piece,destination_piece))
        
        self.board[to_be_moved_row][to_be_moved_column] = ""
        self.board[new_pos_row][new_pos_column] = start_piece

    def undo_move(self):
        if not self.move_history:
            return
        move, start_piece, destination_piece = self.move_history.pop()
        
        start_row,start_column = move.start
        end_row,end_column = move.end
        self.board[start_row][start_column] = start_piece
        self.board[end_row][end_column] = destination_piece

