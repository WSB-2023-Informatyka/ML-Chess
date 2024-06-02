import numpy as np
import tensorflow as tf
import chess

PATH = "D:/ML WSB Chess/ML-Chess/ai/"  # change this to dynamic path

class neural_network():

    def moves_to_fen(self,moves, board):
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
        list_to_be_evaluated = self.moves_to_fen(list_of_moves_to_eval,current_board_state)
        from ai import AI
        ai = AI(1)
        highest_prediction = -float('inf')
        best_move = None

        for one_move in list_to_be_evaluated:
            prepared_data_to_eval = ai.fen_matrix_into_one_row(ai.fen_to_onehot(one_move[1])) # fen to one hot smiga
            prediction = self.nn_evaluate_move(prepared_data_to_eval)
            if prediction > highest_prediction:
                highest_prediction = prediction
                best_move = one_move[0]
        return best_move

    def nn_evaluate_move(self, input_data):
        # Wczytaj dane z załączonych plików
        X_MEAN, X_STD = np.load(PATH + "X_mean.npy"), np.load(PATH + "X_std.npy")
        # Wczytaj oraz znormalizuj dane
        # input_data = "tutaj wkładamy Jednowymiarową tablicę z 768 wartościami ( Mam algorytm do przerabiania fen na taką spłaszczoną tablicę)"
        input_data = (input_data - X_MEAN) / X_STD

        # Jak mam dane równe 0 to tensorflow narzeka na dzielenie przez 0, więc dodajemy wszędzie malutką wartosc,
        input_data += 1e-8

        # Przekształć dane aby pasowały pod model 10 - ilość 'batchów danych' 768 - ilość wartości w podanej zmiennej
        # ilość wymiarów naszej listy
        input_data = input_data.reshape((1, 768, 1))

        model = tf.keras.models.load_model(PATH + "ML_chessCNN1.h5")

        # Przewiduj to jak dobry jest ten ruch.. Im wyższa wartość tym lepiej
        predictions = model.predict(input_data)
        return predictions

# Import the AI class here

