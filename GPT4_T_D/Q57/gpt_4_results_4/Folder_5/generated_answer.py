
import numpy as np

def submatrix_with_particular_sum(mat):
    results = []
    n, m = mat.shape
    for size in range(1, min(n, m) + 1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                submat = mat[i:i+size, j:j+size]
                if np.sum(submat) == -43:
                    results.append(submat.tolist())
                    
    return results if results else []
