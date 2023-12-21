import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 154:
                count += matrix[row][:col] + matrix[row][col+1:] + matrix[:row] + matrix[row+1:] + matrix[col:][:row] + matrix[col+1:][row:].count(154)
    return count
