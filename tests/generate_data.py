import numpy as np
import random
import os

numsamples = 100000

output = np.zeros((numsamples,8*8))
outkeys = np.zeros((numsamples, 8+8))
for i in range(numsamples):
    sample = np.zeros((8,8))
    key = np.zeros((16,))
    for j in range(8):
        if (random.random() <= 0.125):
            sample[j,:] = 1
            key[j] = 1
    for j in range(8):
        if (random.random() <= 0.125):
            sample[:,j] = 1
            key[j+8] = 1
    if (random.random() <= 0.5):
        sample[7,:] = 1
        key[7] = 1
    outkeys[i,:] = key
    output[i,:] = sample.reshape((-1))

if not os.path.exists("../data/"):
    os.makedirs("../data/")

np.savetxt("../data/lines_unbalanced.csv", output)
np.savetxt("../data/keys_unbalanced.csv", outkeys)
