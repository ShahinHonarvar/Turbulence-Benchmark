import numpy as np
def submatrix_with_n_numbers(matrix):
    n_submatrix = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cnt = 0
            for i in range(row, row + 122):
                if i >= len(matrix):
                    break
                cnt += 1
            if cnt == 122:
                n_submatrix += 1
    return n_submatrix
