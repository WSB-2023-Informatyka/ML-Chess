import numpy as np
import tensorflow as tf

# Wczytaj dane z załączonych plików
X_MEAN, X_STD = np.load("X_mean.npy"), np.load("X_std.npy")

# Wczytaj oraz znormalizuj dane
input_data = "tutaj wkładamy Jednowymiarową tablicę z 768 wartościami ( Mam algorytm do przerabiania fen na taką spłaszczoną tablicę)"
input_data = (input_data - X_MEAN) / X_STD

# Jak mam dane równe 0 to tensorflow narzeka na dzielenie przez 0, więc dodajemy wszędzie malutką wartosc,
input_data += 1e-8

# Przekształć dane aby pasowały pod model 10 - ilość 'batchów danych' 768 - ilość wartości w podanej zmiennej
# ilość wymiarów naszej listy
input_data = input_data.reshape((10, 768, 1))

model = tf.keras.models.load_model("ML_chessCNN1.h5")

# Przewiduj to jak dobry jest ten ruch.. Im wyższa wartość tym lepiej
predictions = model.predict(input_data)
print(predictions)
