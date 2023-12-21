
import numpy as np

def submatrix_with_particular_sum(matrix):
    def get_submatrices(a):
        submatrices = []
        for width in range(1,a.shape[1]+1):
            for height in range(1,a.shape[0]+1):
                for x in range(a.shape[0]-height+1):
                    for y in range(a.shape[1]-width+1):
                        submatrices.append(a[x:x+height,y:y+width])
        return submatrices

    results = []
    submatrices = get_submatrices(matrix)
    for sm in submatrices:
        if np.sum(sm) == -863:
            results.append(sm)
    return results
