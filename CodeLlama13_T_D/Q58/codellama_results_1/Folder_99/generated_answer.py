
import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.asarray(matrix)
    num_rows, num_cols = matrix.shape
    
    def count_submatrices(row_index, col_index, current_count):
        if row_index == num_rows or col_index == num_cols:
            return 0
        
        current_count += (matrix[row_index, col_index] == 146)
        
        for i in range(row_index + 1, num_rows):
            for j in range(col_index + 1, num_cols):
                if matrix[i, j] != matrix[row_index, col_index]:
                    continue
                    
                current_count += count_submatrices(i, j, current_count)
        
        return current_count
    
    return count_submatrices(0, 0, 0)
