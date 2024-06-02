import chess
import numpy as np
import random
from ai.use_model import neural_network

# import tensorflow as tf

PATH_TO_STOCKFISH_DATA = r"D:\ML WSB Chess\ML-Chess\fen_to_stockfish_evaluation.csv"
READY_DATASET = r"D:\ML WSB Chess\ML-Chess\datasets\dataset.csv"

PIECE_TO_VECTOR = {
    "P": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "N": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "B": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "R": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Q": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "K": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "p": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "n": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "b": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "r": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    "q": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "k": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    " ": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR "
fen_for_testing = [
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR ",
    "8/8/8/4k3/3R4/8/8/4K3",
    "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR",
    "r3k2r/ppp1qppp/2n5/8/2b1B3/5Q2/PPP1NPPP/R3K2R",
]



def fen_matrix_into_one_row(matrix):
    flattened_matrix = matrix.flatten()
    return flattened_matrix



# for fenn in fen_for_testing:
# 	print(f"{fen_matrix_into_one_row(fen_to_onehot(fenn))}\n")


class AI:
    def __init__(self, depth) -> None:
        self.depth = depth  # depth = how deep should Min_max

    # TODO: load model while creating the app
    # for x in self.add_attack_info(fen):
    # 	print(x, "\n")

    def move(self, board: chess.Board) -> chess.Move:
        best_score = float('-inf')
        best_moves = []  # Store best moves

        for move in board.legal_moves:
            new_board = board.copy()
            new_board.push(move)
            score = self.minimax(new_board, False, self.depth - 1)
            if score > best_score:
                best_score = score
                best_moves = [move]  # Reset with the new best move
            if score == best_score:  # Note: this is now an "if" clause, not "elif"
                best_moves.append(move)  # Add the move

            nn = neural_network()
            best_move = nn.give_me_predictions(best_moves,board)

            # best_move = random.choice(best_moves) # Randomly select one of the best moves


        return best_move
    def minimax(self, board, is_maximizing_player, depth):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board)

        if is_maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, False, depth - 1)
                board.pop()  # undo the move
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, True, depth - 1)
                board.pop()  # undo the move
                min_eval = min(min_eval, eval)

            return min_eval

    def evaluate(self, board):
        return self.material_balance(board)

# https://github.com/niklasf/python-chess/discussions/864
    def material_balance(self,board):
        white = board.occupied_co[chess.WHITE]
        black = board.occupied_co[chess.BLACK]
        return (
            chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
            3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
            3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
            5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
            9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens))
        )

    def fen_to_onehot(self,fen):
        # print(f"FEN TO BE ONEHOTED:{fen}")

        # Initialize an empty 8x8x12 array
        board = np.zeros((8, 8, 12))

        # Parse the FEN string
        rows = fen.split("/")

        # Iterate over the rows
        for i in range(min(8, len(rows))):  # Only iterate over the first 8 rows
            row = rows[i]

            for j, char in enumerate(row):
                # If its a digit its empty
                if char.isdigit():
                    # Go to empty squares
                    j += int(char) - 1
                else:
                    if j < 8:
                        # Get the one-hot vector for the piece
                        piece_vector = PIECE_TO_VECTOR[char]
                        # Set the corresponding values in the one-hot array
                        board[i, j, :] = piece_vector
        return board

    def fen_matrix_into_one_row(self,matrix):
        flattened_matrix = matrix.flatten()
        return flattened_matrix

    def csv_stockfish_into_input_data2(self,csv_stockfish_path, dataset_path):
        i = 0
        temp_str = ""
        with open(csv_stockfish_path, "r") as file:
            for line in file:
                temp_str = line.strip() + " "  # clean useless symbols
                temp_str = temp_str.split(
                    " "
                )  # split fen string from additional castling/pawn move data.

                temp_str, color, castle, stockfish_eval = (
                    self.fen_to_onehot(temp_str[0]),
                    temp_str[1],
                    temp_str[2],
                    temp_str[6],
                )
                stockfish_eval = float(stockfish_eval)

                fen_in_oned_matrix = fen_matrix_into_one_row(temp_str)

                if color == "w":
                    color_info = 0
                else:
                    color_info = 1
                fen_in_oned_matrix = np.append(fen_in_oned_matrix, color_info)
                fen_in_oned_matrix = np.append(fen_in_oned_matrix, stockfish_eval)

                with open(dataset_path, "a") as output:
                    # print(len(fen_in_oned_matrix))
                    np.savetxt(output, [fen_in_oned_matrix], fmt="%f", delimiter=" ")

    def csv_stockfish_into_input_data(self,
        csv_stockfish_path, dataset_path, additional_features_enabled
    ):

        if additional_features_enabled:
            pass
        i = 0
        temp_str = ""
        stockfish_eval = [""]
        with open(csv_stockfish_path, "r") as file:
            for line in file:
                temp_str = line.strip() + " "  # clean useless symbols
                temp_str = temp_str.split(
                    " "
                )  # split fen string from additional castling/pawn move data.

                temp_str, color, castle, stockfish_eval[0] = (
                    self.fen_to_onehot(temp_str[0]),
                    temp_str[1],
                    temp_str[2],
                    temp_str[6],
                )
                stockfish_eval = float(stockfish_eval[0])

                fen_in_oned_matrix = fen_matrix_into_one_row(temp_str)
                x = fen_in_oned_matrix
                x = x.astype("float32")
                # print(type(x[0]))
                # print(x[0])
                # print(len(x))

                # Change into numpy array so it can be concatenated
                stockfish_eval = np.array([stockfish_eval])

                # Add a new axis to stockfish_eval to make it a 2D array
                stockfish_eval = stockfish_eval[:, np.newaxis]

                # Convert fen_in_oned_matrix to a 2D array
                fen_in_oned_matrix = fen_in_oned_matrix[np.newaxis, :]

                # Concatenate stockfish_eval with fen_in_oned_matrix
                x = np.concatenate((fen_in_oned_matrix, stockfish_eval), axis=1)
                x = x.reshape(-1)

                print(x)
                print(f"Flat.len:{len(x)}")
                print(type(x))

                # TODO dodaj info, o tym czyja teraz kolej b or w, ale najpierw niech dziala w podstawowym stanie

                with open(dataset_path, "a") as output:
                    # print(len(fen_in_oned_matrix))
                    np.savetxt(output, [x], fmt="%f", delimiter=" ")


    def add_attack_info(self, fen_str):
        # Convert the FEN string to a one-hot encoded array
        board = self.fen_to_onehot(fen_str)

        # Initialize an empty 8x8x12 array for the attack information
        attack_info = np.zeros((8, 8, 12))

        # Define the possible moves for each piece type
        pawn_moves = [(1, 1), (1, -1)]
        knight_moves = [
            (2, 1),
            (2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (-2, 1),
            (-2, -1),
        ]
        king_moves = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        rook_moves = [(0, i) for i in range(-8, 8)] + [(i, 0) for i in range(-8, 8)]
        bishop_moves = [(i, i) for i in range(-8, 8)] + [(i, -i) for i in range(-8, 8)]
        queen_moves = rook_moves + bishop_moves

        # Iterate over all squares on the board
        for row in range(8):
            for col in range(8):
                # Get the one-hot vector for the current square
                piece = board[row, col, :]

                # Check if the square is occupied by a piece of the current player
                if np.sum(piece[:6]) == 1:
                    # Iterate over all possible moves for the piece type
                    for move in (
                        pawn_moves
                        if np.sum(piece[:1]) == 1
                        else (
                            knight_moves
                            if np.sum(piece[1:2]) == 1
                            else (
                                king_moves
                                if np.sum(piece[4:5]) == 1
                                else (
                                    rook_moves
                                    if np.sum(piece[2:3]) == 1
                                    else (
                                        bishop_moves
                                        if np.sum(piece[3:4]) == 1
                                        else queen_moves
                                    )
                                )
                            )
                        )
                    ):

                        # Calculate the target square coordinates
                        new_row, new_col = row + move[0], col + move[1]

                        # Check if the target square is within the board bounds
                        if 0 <= new_row < 8 and 0 <= new_col < 8:
                            # Check if the target square is occupied by an enemy piece
                            enemy_piece = board[new_row, new_col, 6:]
                            if np.sum(enemy_piece) == 1:
                                # Set the corresponding value in the attack array
                                attack_info[new_row, new_col, :6] = piece[:6]

        # Concatenate the original board and the attack array along the last dimension
        new_board = np.concatenate((board, attack_info), axis=2)

        return new_board


# csv_stockfish_into_input_data(PATH_TO_STOCKFISH_DATA, READY_DATASET, True)



# chesboard_in_default_state = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
# chessboard_in_dangerous_state = chess.Board("rnbqkbnr/pppppppp/8/8/4p3/8/PPPP1PPP/RNBQKBNR w KQkq")
# ai = AI(2)
# ai.move(chessboard_in_dangerous_state)
