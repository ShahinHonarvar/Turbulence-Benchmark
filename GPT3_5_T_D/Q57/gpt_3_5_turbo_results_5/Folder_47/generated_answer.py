
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for m in range(i+1, rows+1):
                for n in range(j+1, columns+1):
                    submatrix = matrix[i:m, j:n]
                    if np.sum(submatrix) == 27:
                        submatrices.append(submatrix.tolist())
    return submatrices
