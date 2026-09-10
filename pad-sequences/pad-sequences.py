import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    out = [[] for _ in seqs]
    if not len(seqs):
        return np.empty((0,0), dtype=int)
    N = len(seqs)
    if max_len:
        L = max_len
    else :
        L = max(len(seq) for seq in seqs)
    # print(N)
    for i in range(N):
        for j in range(L):
            if j < len(seqs[i]):
               out[i].append(seqs[i][j])
            else:
                out[i].append(pad_value)
        
    arr = np.array(out, dtype=int)
    return arr