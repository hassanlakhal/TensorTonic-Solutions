import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    arr = np.asarray(x)
    sigmoid = 1 / (1 + np.exp(-arr))
    # Write code here
    return arr * sigmoid