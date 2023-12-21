
import numpy as np

def submatrix_with_n_numbers(my_matrix):
    count = 0
    rows, cols = my_matrix.shape
    row_combinations = [(r1, r1+1, r1+2, r1+3) for r1 in range(0, rows-3)]
    col_combinations = [(c1, c1+1, c1+2, c1+3) for c1 in range(0, cols-3)]
    
    for row_ind in row_combinations:
        for col_ind in col_combinations:
            sub_matrix = my_matrix[np.ix_(row_ind, col_ind)]
            if sub_matrix.size == 24:
                count += 1
    return count
