import torch

def skipgram_pairs(token_ids: torch.Tensor, window: int) -> torch.Tensor:
    """
    Returns the ordered center-context pairs as an int64 tensor.
    """
    pairs = []
    for i in range(len(token_ids)):
        start = max(0, i - window)
        end = min(len(token_ids), i + window + 1)

        for j in range(start, end):
            if  j != i:
                pairs.append([token_ids[i].item(), token_ids[j].item()])
        
    pairs_ = torch.tensor(pairs, dtype=torch.long).reshape(-1, 2)
    return pairs_