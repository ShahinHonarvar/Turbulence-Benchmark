
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 126 + 1):
        for j in range(matrix.shape[1] - 126 + 1):
            if np.all(matrix[i:i+126, j:j+126] == 126):
                count += 1

    return count
