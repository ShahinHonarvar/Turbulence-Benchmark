
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for r_size in range(1, rows+1):
        for c_size in range(1, cols+1):
            if r_size * c_size != 41:
                continue
            for i in range(rows-r_size+1):
                for j in range(cols-c_size+1):
                    submatrix = matrix[i:i+r_size, j:j+c_size]
                    if submatrix.size == 41:
                        count += 1
    
    return count
