
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    # Iterate through all possible top left corners of submatrix
    for r1 in range(rows):
        for c1 in range(cols):
            # Iterate through all possible bottom right corners
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    # Check if the submatrix has 180 elements
                    if (r2-r1+1)*(c2-c1+1) == 180:
                        count += 1

    return count
