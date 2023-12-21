
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_list = []
    rows, cols = matrix.shape
    for SubM_RowSize in range(1, rows+1):
        for SubM_ColSize in range(1, cols+1):
            for row in range(0, rows-SubM_RowSize+1):
                for col in range(0, cols-SubM_ColSize+1):
                    submatrix = matrix[row:row+SubM_RowSize, col:col+SubM_ColSize]
                    if submatrix.sum() == -3:
                        submatrices_list.append(submatrix)
    return submatrices_list
