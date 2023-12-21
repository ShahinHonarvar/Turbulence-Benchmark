import numpy as np
def submatrix_with_n_numbers(A):
    return sum(1 for i in range(len(A)) for j in range(len(A[i])) if A[i][j] == 23)
