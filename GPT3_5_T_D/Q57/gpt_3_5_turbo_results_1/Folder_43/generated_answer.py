
import numpy as np

def submatrix_with_particular_sum(matrix):
    def find_submatrix(matrix, sum_value):
        rows, cols = matrix.shape
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrix = matrix[i:k, j:l]
                        if np.sum(submatrix) == sum_value:
                            submatrices.append(submatrix)
        return submatrices
    
    return find_submatrix(matrix, -81)
