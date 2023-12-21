import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    submatrix_list = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_sum = 0
            col_sum = 0
            for row_element in range(len(matrix[row])):
                row_sum += matrix[row][row_element]
            for col_element in range(len(matrix[row]) - 1):
                col_sum += matrix[row][col_element]
            if row_sum == -64:
                submatrix_list.append((row, col))
    return submatrix_list
