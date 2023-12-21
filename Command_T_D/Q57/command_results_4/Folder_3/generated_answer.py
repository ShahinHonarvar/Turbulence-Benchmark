import numpy as np
def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        return []
    matrix = np.array(matrix, dtype=np.int64)
    return [row[1:-1] for row in matrix]
