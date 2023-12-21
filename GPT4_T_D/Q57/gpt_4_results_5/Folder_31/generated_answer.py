
import numpy as np

def submatrix_with_particular_sum(A):
    m,n = A.shape[0],A.shape[1]
    submatrix_list = []
    for sub_m in range(1,m+1):
        for sub_n in range(1,n+1):
            for i in range(m-sub_m+1):
                for j in range(n-sub_n+1):
                    submatrix = A[i:i+sub_m,j:j+sub_n]
                    if np.sum(submatrix) == -44:
                        submatrix_list.append(submatrix)
    return submatrix_list
