
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for x in range(row, len(matrix)):
                for y in range(col, len(matrix[row])):
                    submatrix = matrix[row:x+1, col:y+1]
                    if submatrix.size == 173:
                        count += 1
    return count
