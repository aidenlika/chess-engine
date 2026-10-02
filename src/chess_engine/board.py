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


    def get_knight_moves(self,row,col):
        possible_positions = [(2+row,1+col),(2+row,-1+col),(1+row,2+col),(1+row,-2+col),(-2+row,-1+col),(-1+row,-2+col),(-2+row,1+col),(-1+row,2+col)]
        knight = self.board[row][col]
        valid = []

        for element in possible_positions:
            r,c = element
            if 0<= r <= 7 and 0<=  c <=7:
                piece = self.board[r][c]
                if (piece.isupper() and knight.islower()) or (piece.islower() and knight.isupper() or piece==""):
                    valid.append(element)
        return valid

    def get_rook_moves(self,row,col):
        directions = [(0,1),(0,-1),(-1,0),(1,0)] #right,left, up, down
        valid = []
        rook = self.board[row][col]
        for element in directions:
            r,c = element
            rowchange = row+r
            colchange = col +c
            while 0<=(rowchange)<=7 and 0<=(colchange)<=7:
                piece = self.board[rowchange][colchange]
                if piece =="":
                    valid.append((rowchange,colchange))
                    rowchange+=r
                    colchange+=c
                    
                elif (piece.islower() and rook.isupper() or (piece.isupper() and rook.islower())):
                    valid.append((rowchange,colchange))
                    break
                elif (piece.islower() and rook.islower() or (piece.isupper() and rook.isupper())):
                    break
        return valid


                
