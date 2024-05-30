import keras.models
import numpy as np
import tensorflow as tf

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


chunksize = 1000
X, y = [], []

#
# conda create --prefix D:\ML WSB Chess\ML-Chess\ai\conda python=3.10
# Open the CSV file
with open("D:\\ML WSB Chess\\ML-Chess\\datasets\\dataset.csv", "r") as f:
    # Loop through each chunk of data
    for i in range(0, int(13e9 / chunksize)):
        # Read a chunk of data from the CSV file
        data = np.loadtxt(f, dtype=np.float64, delimiter=" ", max_rows=chunksize)

        if data.size == 0:
            continue

        # Extract input features and output label
        X_chunk = data[:, :-1]
        y_chunk = data[:, -1]

        # Normalize the input data to have mean 0 and standard deviation 1
        X_mean = X_chunk.mean(axis=0, keepdims=True)
        X_std = X_chunk.std(axis=0, keepdims=True)
        X_std[X_std == 0] = 1
        X_chunk = (X_chunk - X_mean) / X_std

        X_std = X_chunk.std(axis=0, keepdims=True) + 1e-8

        # Normalize the reward values to have mean 0 and standard deviation 1
        y_mean = y_chunk.mean()
        y_std = y_chunk.std()
        y_chunk = (y_chunk - y_mean) / y_std

        # Append input features and output label to lists
        X.append(X_chunk)
        y.extend(y_chunk)

# Concatenate the list of input features into a single array
X = np.concatenate(X)

# Add a small constant to avoid division by zero
X += 1e-8

# Reshape the input data to match the expected input shape of the model
X = X.reshape((-1, 768, 1))


# Define the architecture of the CNN model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Reshape((768, 1), input_shape=(1, 768)))
model.add(tf.keras.layers.Conv1D(32, 3, activation="relu"))
model.add(tf.keras.layers.MaxPooling1D(2))
model.add(tf.keras.layers.Conv1D(64, 3, activation="relu"))
model.add(tf.keras.layers.MaxPooling1D(2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation="relu"))
model.add(tf.keras.layers.Dense(1))

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Print the shapes of X and y
for i, (x, y_val) in enumerate(zip(X, y)):
    print(f"Shape of X[{i}]: {np.shape(x)}")
    print(f"Shape of y[{i}]: {np.shape(y_val)}")

if len(X) > 0:
    model.fit(X, y, epochs=10, batch_size=32)
else:
    print("Error: X is an empty array")

# Save the model to a file
tf.saved_model.save(model, "first_model_on_13gb_database")
np.save("X_mean.npy", X_mean)
np.save("X_std.npy", X_std)
