
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for row in range(shape[0]):
        for column in range(shape[1]):
            for i in range(row, shape[0]):
                for j in range(column, shape[1]):
                    submatrix = matrix[row:i+1, column:j+1]
                    if np.size(submatrix) == 63:
                        count += 1
    return count
