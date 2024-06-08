import numpy as np
import tensorflow as tf
import chess
import os


PATH = os.path.join(os.getcwd(), "")
FENS_TO_EVAL = [
            ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq"],  # 0.24
            ["r1bq1rk1/pp1nppbp/3p1np1/2p5/2PPP3/2N1BN2/PP3PPP/2RQKB1R"],  # -1.84
            ["3rr1k1/pp1n1ppp/2p5/2bp4/B7/8/PPP2PPP/R1BR2K1"],  # -1.97
            ["3rr1k1/pp1n2pp/2p2p2/2bp2B1/B7/8/PPP2PPP/R2R2K1"],  # -5.08
            ["4r1k1/3R2pp/5p2/2p1n3/1b1p4/1P4BP/2P2PP1/3R2K1"],  # -6.52
            ["8/8/1r3kp1/3b1p2/8/4P1P1/R2NKP2/8"]  # 0.41
        ]

class neural_network():

    def moves_to_fen(self, moves, board):
        """
        Convert a list of chess moves to a list of FEN strings.
        """

        fen_list = [board.fen()]  # Initial board state

        for move in moves:
            board.push(move)
            fen_list.append(board.fen())
            board.pop()

        merged_fen_list = [[x, y] for x, y in zip(moves, fen_list)]

        return merged_fen_list

    def give_me_predictions(self, list_of_moves_to_eval, current_board_state):
        list_to_be_evaluated = self.moves_to_fen(list_of_moves_to_eval, current_board_state)
        from ai import AI
        ai = AI(1, 0, 0)  # Needs fixing, we shoudn't call class in such place ( the class that we call is calling us)
        highest_prediction = -float('inf')
        best_move = None

        for one_move in list_to_be_evaluated:
            prepared_data_to_eval = ai.fen_matrix_into_one_row(ai.fen_to_onehot(one_move[1]))  # fen to one hot smiga
            prediction = self.nn_evaluate_move(prepared_data_to_eval)
            if prediction > highest_prediction:
                highest_prediction = prediction
                best_move = one_move[0]
        return best_move
    def give_me_predictions_test(self,fens_to_eval):

        """

        rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1, 0.24
        rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1, 0.59
        rnbqkbnr/pppppp1p/6p1/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2, 0.27

        r1bq1rk1/pp1nppbp/3p1np1/2p5/2PPP3/2N1BN2/PP3PPP/2RQKB1R w K - 0 8, -1.84
        r1bq1rk1/pp1nppbp/3p1np1/2p1P3/2PP4/2N1BN2/PP3PPP/2RQKB1R b K - 0 8, -1.34
        r1bq1rk1/pp1nppbp/5np1/2p1p3/2PP4/2N1BN2/PP3PPP/2RQKB1R w K - 0 9, -0.95

        3rr1k1/pp1n1ppp/2p5/2bp4/B7/8/PPP2PPP/R1BR2K1 w - - 2 18, -1.97
        3rr1k1/pp1n1ppp/2p5/2bp2B1/B7/8/PPP2PPP/R2R2K1 b - - 3 18, -1.92
        3rr1k1/pp1n2pp/2p2p2/2bp2B1/B7/8/PPP2PPP/R2R2K1 w - - 0 19, -5.08
        """

        fens_to_eval_resul = [[0.24],[-1.84],[-1.97],[-5.08],[-6.52],[0.41]]
        from ai import AI
        ai = AI(1, 0, 0)  # Needs fixing, we shoudn't call class in such place ( the class that we call is calling us)
        highest_prediction = -float('inf')
        best_move = None

        for i, one_move in enumerate(fens_to_eval):

            prepared_data_to_eval = ai.fen_matrix_into_one_row(ai.fen_to_onehot(str(one_move[0])))  # fen to one hot smiga
            prediction = self.nn_evaluate_move_test(prepared_data_to_eval)
            print(f"predicted:{prediction[0]},fen used for prediction::{fens_to_eval[i][0]}")
            print(f"Expected result: {fens_to_eval_resul[i]}")

    def nn_evaluate_move(self, input_data):
        X_MEAN, X_STD = np.load(PATH + "\\ai\\X_mean.npy"), np.load(PATH + "\\ai\\X_std.npy")

        input_data = (input_data - X_MEAN) / X_STD
        input_data += 1e-8
        input_data = input_data.reshape((-1, 768, 1))
        model = tf.keras.models.load_model(PATH + "\\ai\\ML_chessCNN1.h5")

        # Create a dataset from the input data
        dataset = tf.data.Dataset.from_tensor_slices(input_data)
        # Batch the data and prefetch the next batch
        dataset = dataset.batch(32).prefetch(1)

        predictions = model.predict(dataset)
        return predictions

    def nn_evaluate_move_test(self, input_data):

        X_MEAN, X_STD = np.load(PATH + "\\ai\\X_mean.npy"), np.load(PATH + "\\ai\\X_std.npy")

        input_data = (input_data - X_MEAN) / X_STD
        input_data += 1e-8
        input_data = input_data.reshape((1, 768, 1))
        model = tf.keras.models.load_model(PATH + "\\ai\\ML_chessCNN1.h5")

        predictions = model.predict(input_data) * 14,8
        return predictions
# nn = neural_network()
# nn.give_me_predictions_test(FENS_TO_EVAL)
