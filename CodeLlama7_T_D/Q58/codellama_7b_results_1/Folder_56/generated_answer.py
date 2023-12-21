
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = matrix[i:i + 68, j:j + 68]
            if all(num == 68 for row in submatrix for num in row):
                count += 1
    return count
