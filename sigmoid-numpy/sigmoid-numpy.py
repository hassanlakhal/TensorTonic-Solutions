import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """

    ele = np.asarray(x)
    sig = 1 / (1 + np.exp(-ele))
    return sig
    # Write code here
    # return sig