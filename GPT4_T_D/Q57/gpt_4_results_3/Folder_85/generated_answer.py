
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    output = []
    
    for submatrix_width in range(1, n + 1):
        for submatrix_height in range(1, m + 1):
            for i in range(m - submatrix_height + 1):
                for j in range(n - submatrix_width + 1):
                    submatrix = matrix[i:(i + submatrix_height), j:(j + submatrix_width)]
                    if np.sum(submatrix) == -87:
                        output.append(submatrix)

    return output
