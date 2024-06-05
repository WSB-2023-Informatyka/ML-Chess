import numpy as np
import tensorflow as tf

DATA_PATH = "D:\\ML WSB Chess\\ML-Chess\\datasets\\dataset.csv"
CHUNKSIZE = 769


class TrainingModel:
    def __init__(self, data_path, chunksize,activation_fun,l1,l2,p,l4):
        self.l1 = l1
        self.l2 = l2
        self.p = p
        self.l4 = l4


        self.data_path = data_path
        self.chunksize = chunksize
        self.activation_fun = activation_fun

    def training(self):
        data = []

        # Load data in chunks and append to data list
        for i in range(0, 76800, self.chunksize):
            chunk = np.loadtxt(self.data_path, dtype=np.float64, delimiter=" ",
                               skiprows=i, max_rows=self.chunksize)
            data.append(chunk)

        data = np.concatenate(data)
        print("Data loading finished")
        print(data[:5])
        print(data.shape)

        X, y = [], []

        if data.size == 0:
            print("ERROR")
            return

        X_chunk = data[:, :-1]
        y_chunk = data[:, -1]

        print(f"Shape of y_chunk: {np.shape(y_chunk)}")

        # Normalize the input data to have mean 0 and standard deviation 1
        X_mean = X_chunk.mean(axis=0, keepdims=True)
        X_std = X_chunk.std(axis=0, keepdims=True)
        X_std[X_std == 0] = 1
        X_chunk = (X_chunk - X_mean) / X_std

        # Normalize the reward values to have mean 0 and standard deviation 1
        y_mean = y_chunk.mean()
        y_std = y_chunk.std()
        y_chunk = (y_chunk - y_mean) / y_std

        # Append input features and output label to lists
        X.append(X_chunk)
        y.extend(y_chunk)

        # Concatenate the list of input features into a single array
        X = np.concatenate(X)
        y = np.array(y)
        from sklearn.model_selection import train_test_split


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("Shapes after concatenation")
        print(f"Shape of X: {X.shape}")
        print(f"Shape of y: {y.shape}")

        # Add a small constant to avoid division by zero
        X += 1e-8

        # Reshape the input data to match the expected input shape of the model
        X = X.reshape((-1, 768, 1))
        print("reshape done")

        # Define the architecture of the CNN model
        model = tf.keras.Sequential([
            tf.keras.layers.Reshape((self.l1, 1), input_shape=(768, 1)),
            tf.keras.layers.Conv1D(self.l2, 3, activation=self.activation_fun),
            tf.keras.layers.MaxPooling1D(self.p),
            tf.keras.layers.Conv1D(self.l4, 3, activation=self.activation_fun),
            tf.keras.layers.MaxPooling1D(self.p),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation=self.activation_fun),
            tf.keras.layers.Dense(1)
        ])

        # Compile the model with multiple metrics
        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["accuracy", "precision", "recall"])
        mse = model.evaluate(X_test, y_test)
        # Train the model if X is not empty
        if X.size > 0:
            model.fit(X, y, epochs=20, batch_size=32)
        else:
            print("Error: X is an empty array")

        loss, accuracy, precision, recall = model.evaluate(X_test, y_test)

        # Print the loss and metrics
        print(f"Loss: {loss}")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"Mean squared error: {mse}")



        # model_name = f"\models\CNN loss{loss},acc{accuracy},prec{precision},mse:{mse},l1{self.l1},l2{self.l2},p{self.p},l4{self.l4}"
        model_name = f"model"
         # Save the model to a file
        tf.saved_model.save(model,f"{model_name}.keras")
        np.save(f"{model_name}X_mean.npy", X_mean)
        np.save(f"{model_name}X_std.npy", X_std)
        model.save(f"{model_name}.h5")


nn = TrainingModel(DATA_PATH, CHUNKSIZE,"relu",768,128,2,64)
nn.training()
# nn = TrainingModel(DATA_PATH, CHUNKSIZE,"relu",768,32,2,64)
# nn.training()
#
# nn = TrainingModel(DATA_PATH, CHUNKSIZE,"relu",768,64,2,64)
# nn.training()
# nn = TrainingModel(DATA_PATH, CHUNKSIZE,"relu",768,64,2,128)
# nn.training()
#
# nn = TrainingModel(DATA_PATH, CHUNKSIZE,"relu",768,128,2,64)
# nn.training()
