import numpy as np
def submatrix_with_particular_sum(arr):
    return [row[row[i] == -87] for i, row in enumerate(arr) if row[i] == -87]
