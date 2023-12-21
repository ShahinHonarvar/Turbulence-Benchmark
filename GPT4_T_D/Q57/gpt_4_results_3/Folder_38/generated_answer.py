
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    numRows, numCols = matrix.shape
    for width in range(1, numCols + 1):
        for height in range(1, numRows + 1):
            for i in range(numRows - height + 1):
                for j in range(numCols - width + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if np.sum(submatrix) == 34:
                        result.append(submatrix.tolist())
    return result
