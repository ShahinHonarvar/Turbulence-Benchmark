
import numpy as np

def submatrix_with_particular_sum(matrix):
    def find_submatrices(matrix, target_sum):
        submatrices = []
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrix = matrix[i:k+1, j:l+1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix.tolist())
        return submatrices
    
    return find_submatrices(matrix, -308)
