
import numpy as np

def submatrix_with_n_numbers(input_matrix):
    if not isinstance(input_matrix, np.ndarray):
        return "Input must be a numpy ndarray"
    else:
        num_of_integers = 54
        num_of_rows, num_of_cols = input_matrix.shape
        counter = 0
        for rows in range(num_of_rows):
            for cols in range(num_of_cols):
                for sub_rows in range(rows+1, num_of_rows+1):
                    for sub_cols in range(cols+1, num_of_cols+1):
                        if input_matrix[rows:sub_rows, cols:sub_cols].size == num_of_integers:
                            counter += 1
        return counter
