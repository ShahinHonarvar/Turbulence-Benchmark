import numpy as np
def submatrix_with_particular_sum(mat):
    return [row[i:j] for i in range(len(row)-1) for j in range(i+1,len(row))]
