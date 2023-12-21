
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 1:
                row_sum = np.cumsum(matrix[i, j:]).tolist()
                for k in range(i+1, rows):
                    row_sum = [sum(x) for x in zip(row_sum, np.cumsum(matrix[k, j:]).tolist())]
                    count += row_sum.count(122)
    
    return count
