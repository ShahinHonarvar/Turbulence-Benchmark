
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0

    row, col = matrix.shape  
    
    for sub_row in range(row + 1):
        for sub_col in range(col + 1):
            for i in range(row-sub_row+1):
                for j in range(col-sub_col+1):
                    submatrix = matrix[i:(i+sub_row), j:(j+sub_col)]
                    if submatrix.size == 92:
                        count += 1
                        
    return count
