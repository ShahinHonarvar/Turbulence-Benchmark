
import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for h in range(height):
        for w in range(width):
            for x in range(h, height):
                for y in range(w, width):
                    if np.size(matrix[h:x+1, w:y+1]) == 23:
                        count += 1
    return count
