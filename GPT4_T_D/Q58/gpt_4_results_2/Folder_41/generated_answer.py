
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            
            for i in range(rows - r + 1):
                for j in range(cols - c + 1):
                    
                    submatrix = matrix[i:(i+r), j:(j+c)]
                    if submatrix.size == 73:
                        count += 1
                        
    return count
