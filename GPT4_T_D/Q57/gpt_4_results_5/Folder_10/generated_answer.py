
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    for sub_matrix_height in range(1, rows + 1):
        for sub_matrix_width in range(1, cols + 1):
            
            # sliding over the entire matrix with the sub_matrix size sub_matrix_height x sub_matrix_width
            for r in range(rows - sub_matrix_height + 1):
                for c in range(cols - sub_matrix_width + 1):
                    
                    # Get the submatrix
                    sub_matrix = matrix[r: r + sub_matrix_height, c: c + sub_matrix_width]
                    submatrix_sum = np.sum(sub_matrix)
                    if submatrix_sum == 56:
                        result.append(sub_matrix)
    return result
