# day_08
from collections import deque
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'day_08_input.txt'
input = open(filename).read().split("\n")[0]
# input = """123456789012"""

class Image:
    def __init__(self, height=0, width=0, data=None):
        self.layers = []

        while data:
            layer = np.zeros((height,width), dtype=int)
            for i in range(height):
                for j in range(width):
                    layer[(i,j)] = int(data.popleft())

            self.layers.append(layer)


    def render(self):
        output = self.layers[0]
        for layer in self.layers:
            output = np.where(output != 2, output, layer)

        plt.imsave('day_8.png', output)

        
image = Image(height=6, width=25, data=deque(input))

"""
find the layer that contains the fewest 0 digits. On that layer, what is the
number of 1 digits multiplied by the number of 2 digits?
"""

unique, counts = np.unique(image.layers[0], return_counts=True)
counts = dict(zip(unique, counts))
min_zeros = counts[0]
layer_min_zeros = 0

for i, layer in enumerate(image.layers):
    unique, counts = np.unique(layer, return_counts=True)
    counts = dict(zip(unique, counts))
    if counts[0] < min_zeros:
        min_zeros = counts[0]
        layer_min_zeros = i

print(i)

print(image.layers[layer_min_zeros])

unique, counts = np.unique(image.layers[layer_min_zeros], return_counts=True)
counts = dict(zip(unique, counts))

print(counts)

image.render()