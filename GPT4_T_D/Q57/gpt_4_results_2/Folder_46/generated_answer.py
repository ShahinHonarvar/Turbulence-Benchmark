
import numpy as np

def submatrix_with_particular_sum(npmat):
    n, m = npmat.shape
    res = []
    for i in range(n+1):
        for j in range(m+1):
            for p in range(i+1, n+1):
                for q in range(j+1, m+1):
                    a = npmat[i:p,j:q]
                    if a.sum() == 416:
                        res.append(a)
    return res
