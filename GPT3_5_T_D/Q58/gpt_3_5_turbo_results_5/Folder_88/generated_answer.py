
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    numRows, numCols = matrix.shape
    for i in range(numRows):
        for j in range(numCols):
            if i + 1 < numRows and j + 1 < numCols:
                submatrix = matrix[i:i+2, j:j+2]
                if np.count_nonzero(submatrix == 67) == 4:
                    count += 1
    return count
