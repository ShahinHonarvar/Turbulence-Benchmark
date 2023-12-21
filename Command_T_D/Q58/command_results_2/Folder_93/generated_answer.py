import numpy as np
def submatrix_with_n_numbers(matrix):
    # your code here
    matrix = np.array(matrix)
    if len(matrix) < 53:
        return 0
    return sum(
        sum(
            1
            for j in range(min(i + 52, len(matrix) - 1), i, -1)
            if matrix[j]
        )
        for i in range(0, len(matrix) - 52)
    )
