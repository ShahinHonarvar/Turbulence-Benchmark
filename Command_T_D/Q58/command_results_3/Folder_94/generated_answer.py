import numpy as np
def submatrix_with_n_numbers(A):
    A_copy = np.copy(A)
    count = 0
    for i in range(len(A_copy)):
        for j in range(len(A_copy[0])):
            current_count = 0
            for k in range(i, len(A_copy)):
                if A_copy[k][j] == 1:
                    current_count += 1
                else:
                    break
            if current_count == 93:
                count += 1
    return count
