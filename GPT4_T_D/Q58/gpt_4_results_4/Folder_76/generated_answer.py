
import numpy as np
from scipy.ndimage import measurements

def submatrix_with_n_numbers(numpy_matrix):
    count = 0
    rows, columns = numpy_matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i * j == 159:
                count += (rows - i + 1) * (columns - j + 1)
    return count
