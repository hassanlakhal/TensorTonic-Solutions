import torch
import math

def frequency(count , N):
    
    freq =  count / N
    return freq
    
def subsample_keep_probs(counts: torch.Tensor, t: float = 1e-5) -> torch.Tensor:
    """
    Returns torch.Tensor of shape (vocab_size,) with the keep-probability for each word.
    """
    N = counts.sum().item()
    list = []
    
    for count in counts:
        f = frequency(count.item(), N)
        p = min(1 , math.sqrt(t / f))
        list.append(p)
      
    x = torch.Tensor(list)    
    return x
