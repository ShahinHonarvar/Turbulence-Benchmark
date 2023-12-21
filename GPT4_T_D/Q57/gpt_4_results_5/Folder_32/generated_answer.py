
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = np.shape(matrix)
    for submatrix_height in range(1, rows + 1):
        for submatrix_width in range(1, cols + 1):
            for i in range(rows - submatrix_height + 1):
                for j in range(cols - submatrix_width + 1):
                    submatrix = matrix[i: i+submatrix_height, j: j+submatrix_width]
                    if np.sum(submatrix) == 901:
                        result.append(submatrix.tolist())
    return result
