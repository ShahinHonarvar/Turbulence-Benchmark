
import numpy as np

def submatrix_with_n_numbers(mat, n):
    return len([s for s in all_submatrices(mat) if sum(s) == 85])

def all_submatrices(mat):
    return [
