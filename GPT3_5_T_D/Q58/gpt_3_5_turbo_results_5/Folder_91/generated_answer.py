
def submatrix_with_n_numbers(matrix):
    import numpy as np
    count = 0
    rows, columns = np.shape(matrix)
    
    for i in range(rows-4):
        for j in range(columns-4):
            sub_matrix = matrix[i:i+5, j:j+5]
            if np.size(sub_matrix) == 25:
                count += 1
                    
    return count
