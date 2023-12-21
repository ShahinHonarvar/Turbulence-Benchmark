
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for size in range(1, min(rows, cols) + 1):  # checking for all possible sizes of submatrices
        for i in range(rows - size + 1):  # checking for all possible starting rows
            for j in range(cols - size + 1):  # checking for all possible starting columns
                sub_matrix = matrix[i:i+size, j:j+size]  # getting the submatrix of specified size from specified starting position
                if np.sum(sub_matrix) == -261:  # checking if sum of all integers in the submatrix equals -261
                    sub_matrices.append(sub_matrix)  # appending the submatrix to the list
    return sub_matrices
