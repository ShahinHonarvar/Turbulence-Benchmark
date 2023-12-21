
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = np.shape(matrix)
    
    for row in range(rows + 1):
        for column in range(columns + 1):
            for x in range(row + 1, rows + 1):
                for y in range(column + 1, columns + 1):
                    submatrix = matrix[row:x, column:y]
                    if submatrix.size == 72:
                        count += 1
    return count
