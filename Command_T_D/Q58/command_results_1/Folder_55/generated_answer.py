import numpy as np
def submatrix_with_n_numbers(arr):
    matrices = []
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            current_matrix = []
            for k in range(row, row+38):
                current_matrix += [[arr[k][col]]
            matrices += [current_matrix]
    return len(matrices)
