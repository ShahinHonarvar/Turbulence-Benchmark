import numpy as np
def submatrix_with_particular_sum(arr):
    return [row for row in np.nditer(arr) if len(row) == 3 and row[0] + row[1] + row[2] == -863]
