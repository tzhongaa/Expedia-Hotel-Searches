from __future__ import division
from __future__ import print_function
import numpy as np
def dcg_at_k(r, k):
    """
    Score is discounted cumulative gain(DCG)

    Args:
    ----------
        r: Ranking list
        k: Number of results

    Returns:
    ----------
        Discounted cumulative gain

    """
    r = np.asfarray(r)[:k]
    if r.size:
        return np.sum((np.power(2,r)-1)/np.log2(np.arange(1, k+1)+1))
    return 0

def ndcg_at_k(r,k):
    """
    Normalized discounted cumulative gain(nDCG)

    Args:
    -------------
        r: Ranking list
        k: Number of results

    Returns:
    --------------
        Normalized discounted cumulative gain

    """
    dcg_max = dcg_at_k(sorted(r, reverse=True),k)
    if not dcg_max:
        return 0
    return dcg_at_k(r, k) / dcg_max

if __name__ == "__main__":
    result = np.arange(1,2)
    print(result)
    r = [1, 2, 3]
    r2 = [3,2, 1]
    r3 = []
    print(dcg_at_k(r,1))
    print(dcg_at_k(r,2))
    print(dcg_at_k(r,3))
    print(ndcg_at_k(r,3))
    print(ndcg_at_k(r2,3))
    print(dcg_at_k(r3,1))
    print(ndcg_at_k(r3,2))
