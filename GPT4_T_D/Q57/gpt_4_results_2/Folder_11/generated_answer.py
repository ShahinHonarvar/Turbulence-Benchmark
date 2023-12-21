
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    output = []
    for row in range(rows): 
        for col in range(cols): 
            for r in range(row, rows): 
                for c in range(col, cols): 
                    submatrix = matrix[row: r + 1, col: c + 1] 
                    if submatrix.sum() == 38: 
                        output.append(submatrix.tolist())
    return output
