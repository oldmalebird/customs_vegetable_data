import tensorflow as tf
import numpy as np

m = 10
n = 8
steps = 3
rnn_cell = tf.nn.rnn_cell.BasicLSTMCell(num_units=m)
inputs = tf.constant(value=(np.random.rand(steps, n).astype(np.float32)))
h0 = rnn_cell.zero_state(steps, np.float32)
output, (c, h) = rnn_cell(inputs, h0)
w, b = rnn_cell.variables
print("老公鸟")
print(w.shape, b.shape)
