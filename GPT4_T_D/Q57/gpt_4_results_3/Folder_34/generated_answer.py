
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for sub_x in range(1,n+1):
        for sub_y in range(1,m+1):
            for x in range(n-sub_x+1):
                for y in range(m-sub_y+1):
                    sub = matrix[x:x+sub_x, y:y+sub_y]
                    if np.sum(sub) == -13:
                        result.append(sub)
    return result
