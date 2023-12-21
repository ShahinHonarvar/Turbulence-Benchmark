
import numpy as np

def submatrix_with_n_numbers(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    count = 0

    for row_submatrix in range(1, row_length + 1):
        for column_submatrix in range(1, column_length + 1):
            if row_submatrix * column_submatrix == 185:
                for i in range(row_length - row_submatrix + 1):
                    for j in range(column_length - column_submatrix + 1):
                        count += 1
    return count
