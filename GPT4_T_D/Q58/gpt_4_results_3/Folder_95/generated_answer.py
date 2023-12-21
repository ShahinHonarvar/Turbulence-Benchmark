
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    
    for size_r in range(1, rows + 1):
        for size_c in range(1, columns + 1):
            for r in range(rows - size_r + 1):
                for c in range(columns - size_c + 1):
                    submatrix = matrix[r:(r+size_r), c:(c+size_c)]
                    if submatrix.size == 87:
                        count += 1

    return count
