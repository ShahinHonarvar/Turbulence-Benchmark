import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    n = 23
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
                for k in range(n):
                    if matrix[row][col+k] == 1:
                        matrix[row][col+k] = 0
                        count += 1
                        matrix[row][col] = 1
    return count
