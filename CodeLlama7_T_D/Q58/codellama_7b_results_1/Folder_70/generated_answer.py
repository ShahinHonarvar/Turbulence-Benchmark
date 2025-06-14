
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == 173:
                submatrix = matrix[i:i+2, j:j+2]
                count += (submatrix == 173).all()
    return count
