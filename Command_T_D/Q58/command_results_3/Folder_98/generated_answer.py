import numpy as np
def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    if n < 9:
        return 0
    i = 0
    j = 0
    count = 0
    while i < n:
        if matrix[i] == 1:
            j = i
            count += 1
            while j < n:
                if matrix[j] == 1:
                    count += 1
                    j += 1
                else:
                    break
            if count == 9:
                return count
        i += 1
    return count
