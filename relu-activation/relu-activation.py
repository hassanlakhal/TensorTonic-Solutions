import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    arr = np.array(x)
    mask = arr < 0
    arr[mask] *= 0
    
    return arr