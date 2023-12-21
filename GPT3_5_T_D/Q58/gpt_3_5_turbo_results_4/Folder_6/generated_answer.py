
import numpy as np

def submatrix_with_n_numbers(matrix):
    def search_submatrix(matrix, submatrix_size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - submatrix_size + 1):
            for j in range(cols - submatrix_size + 1):
                submatrix = matrix[i:i+submatrix_size, j:j+submatrix_size]
                if np.count_nonzero(submatrix == 122) == submatrix_size**2:
                    count += 1
        return count

    return search_submatrix(matrix, 2)
