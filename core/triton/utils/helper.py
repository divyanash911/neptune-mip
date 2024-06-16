import numpy as np

def linear_minmax_scale(x: int | float, min: int | float, max: int | float) -> float:
    return (x - min) / (max - min)

def sigmoid_scale(x: int | float) -> float:
    return 1 / (1 + np.exp(-x))

def tanh_scale(x: int | float) -> float:
    return np.tanh(x)

