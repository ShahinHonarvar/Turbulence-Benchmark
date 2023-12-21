import numpy as np
def submatrix_with_particular_sum(matrix):
    return [matrix[row][:]+matrix[row][1:]+matrix[row+1][:]+matrix[row+1][1:]+matrix[row+2][:]+matrix[row+2][1:] for row in range(len(matrix)-2)]
