#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense, Activation

from quant import get_symbols


# Load Dataset
filename = '009530.KS.csv'
data = get_symbols('005930.KS', start='2015-01-01', save_as=filename)
data = pd.read_csv(filename).dropna(axis=0, how='any')
print(data.head())

# Compute Mid Price
high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

# Create Windows
seq_len = 50
sequence_length = seq_len + 1

result = [mid_prices[index:index+sequence_length] for index in range(len(mid_prices) - sequence_length)]

# Normalize Data
normalized_data = [[((float(p) / float(window[0])) - 1) for p in window] for window in result]

result = np.array(normalized_data)

x = result[:, :-1]
y = result[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=0.2, random_state=42)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_val = np.reshape(x_val, (x_val.shape[0], x_val.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

print(x_train.shape, x_test.shape)

# Build a Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(50, 1)),
    LSTM(64, return_sequences=False),
    Dense(1, activation='linear'),
    # Dropout(rate=0.2, noise_shape=None)
])

model.compile(loss='mse', optimizer='rmsprop')

model.summary()

# Training
# model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=10, epochs=20)
# k-fold
step = len(x_train) // 8
for i in range(8):
    start = i * step
    end = (i + 1) * step
    drange = list(range(0, start)) + list(range(end, len(x_train)))
    train = x_train[drange]
    target = y_train[drange]
    val = (x_train[start:end], y_train[start:end])
    model.fit(train, target, validation_data=val, batch_size=16, epochs=1)

# Prediction
pred = model.predict(x_test)

fig = plt.figure(facecolor='white', figsize=(20, 10))
ax = fig.add_subplot(111)
ax.plot(y_test, label='True')
ax.plot(pred, label='Prediction')
ax.legend()
plt.show()
