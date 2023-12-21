import numpy as np
def submatrix_with_particular_sum(A):
    A_array = np.array(A)
    if not A_array.size:
        return []
    rows = A_array.shape[0]
    columns = A_array.shape[1]
    if rows == 1:
        return [A_array]
    if columns == 1:
        return [A_array[i:i+1] for i in range(0, rows)]
    return [A_array[i:i+2] for i in range(0, rows-1)]
