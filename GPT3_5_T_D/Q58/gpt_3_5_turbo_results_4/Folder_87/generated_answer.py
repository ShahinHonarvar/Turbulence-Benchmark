
def submatrix_with_n_numbers(matrix):
    import numpy as np
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if i+3 > rows or j+3 > cols:
                continue
            submatrix = matrix[i:i+4, j:j+4]
            if np.sum(submatrix) == 96 * 16:
                count += 1
                
    return count
