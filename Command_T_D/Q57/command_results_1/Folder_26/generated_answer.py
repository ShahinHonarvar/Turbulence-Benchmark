import numpy as np
def submatrix_with_particular_sum(matrix):
    m = np.array(matrix)
    return [m[i:j+1, i:j+1].tolist() for i in range(len(m)) for j in range(i+1, len(m)) if sum(m[i:j+1, i:j+1]) == 997]
