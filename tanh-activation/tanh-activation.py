import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    arr = np.asarray(x)
    
    e_x0 = np.exp(arr)
    e_x1 = np.exp(-arr) 
    # Write code here
    return (e_x0 - e_x1) / (e_x0 + e_x1)