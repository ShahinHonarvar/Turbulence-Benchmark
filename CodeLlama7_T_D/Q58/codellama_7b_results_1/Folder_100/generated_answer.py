
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize count to 0
    count = 0
    # Iterate over all possible submatrices of size 10x10
    for i in range(len(matrix) - 9):
        for j in range(len(matrix[0]) - 9):
            # Check if the current submatrix contains 10 integers each
            if matrix[i:i+10, j:j+10].size == 100:
                count += 1
    return count
