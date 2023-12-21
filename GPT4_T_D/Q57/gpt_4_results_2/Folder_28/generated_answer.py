
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = np.shape(matrix)
    sub_mtr_list = []
    
    for size_i in range(1, m+1):
        for size_j in range(1, n+1):
            for i in range(m-size_i+1):
                for j in range(n-size_j+1):
                    sub_mtr = matrix[i:i+size_i, j:j+size_j]
                    if np.sum(sub_mtr) == 15:
                        sub_mtr_list.append(sub_mtr.tolist())
    return sub_mtr_list
