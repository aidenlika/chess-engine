class Board:
    def __init__(self):
        self.board = self.create_board()

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

    
boardd = Board()
boardd.display()
