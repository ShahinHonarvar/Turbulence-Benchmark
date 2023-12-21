
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    rows, cols = matrix.shape
    for r_size in range(1, rows + 1):
        for c_size in range(1, cols + 1):
            for r in range(rows - r_size + 1):
                for c in range(cols - c_size + 1):
                    submatrix = matrix[r:r + r_size, c:c + c_size]
                    if np.sum(submatrix) == -26:
                        output.append(submatrix.tolist())
    return output
