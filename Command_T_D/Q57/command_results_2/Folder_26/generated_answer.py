import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr.flags['C_CONTIGUOUS']:
        arr = np.array(arr, dtype=np.int32)
    # row index, col index, row sum, col sum
    matrices = []
    for row in range(len(arr)):
        row_sums = []
        for col in range(len(arr[row])):
            row_sums.append(row_sums[-1] + arr[row][col])
            if row_sums[-1] == 997:
                matrices.append((row, col))
        if 997 in row_sums:
            matrices.append((row,))
    return matrices
