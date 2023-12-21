import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(
        1
        for row in range(len(matrix))
        for col in range(len(matrix[0]))
        if np.all(matrix[row][:col] == 186)
        and np.all(matrix[row][col + 1:] == 186)
        and np.all(matrix[row+1:][:col] == 186)
        and np.all(matrix[row+1:][col + 1:] == 186)
    )
