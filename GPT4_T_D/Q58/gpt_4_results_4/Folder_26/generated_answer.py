
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            for r in range(rows - row + 1):
                for c in range(cols - col + 1):
                    submatrix = matrix[r:r + row, c:c + col]
                    if submatrix.size == 115:
                        count += 1
    
    return count
