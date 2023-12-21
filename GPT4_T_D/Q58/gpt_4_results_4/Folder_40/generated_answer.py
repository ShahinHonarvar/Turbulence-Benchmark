
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if isinstance(element, int) and np.size(element) == 1:
                count += 1

    return count
