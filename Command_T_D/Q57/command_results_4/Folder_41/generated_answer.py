import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if not matrix.shape[0] * matrix.shape[1]:
        return []
    mask = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=np.bool)
    mask[0][0] = True
    row = 0
    col = 0
    while True:
        for r in range(row, matrix.shape[0]):
            if mask[r]:
                mask[r][: matrix.shape[1]] = True
                break
        else:
            break
        for c in range(col, matrix.shape[1]):
            if mask[row][c]:
                mask[row][c:] = True
                break
        else:
            break
        row += 1
        col += 1
    return np.nonzero(mask)[0]
