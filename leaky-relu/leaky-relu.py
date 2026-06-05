import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = [ele * alpha if ele < 0 else ele for ele in x]
    arr = np.array(x)

    return arr