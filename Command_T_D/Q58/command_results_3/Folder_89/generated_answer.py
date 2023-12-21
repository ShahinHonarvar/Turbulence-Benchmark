import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(np.all(A[i:i+18] == np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]), axis=1) for i in range(0,len(A)-17))
