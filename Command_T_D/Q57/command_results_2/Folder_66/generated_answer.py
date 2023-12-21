import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] * matrix.shape[1] == 1:
        return [matrix]
    results = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            submatrix = np.array(matrix[row][:], dtype=int)
            submatrix[row] += 1
            submatrix[col] += 1
            if np.sum(submatrix) == 99:
                results.append(submatrix)
    return results
