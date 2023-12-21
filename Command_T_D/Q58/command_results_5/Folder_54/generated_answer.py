import numpy as np
def submatrix_with_n_numbers(matrix):
    # Your code here
    matrix = np.array(matrix)
    count = 0
    for i in range(len(matrix) - 26):
        for j in range(len(matrix[0]) - 26):
            if np.all(np.equal(matrix[i:i + 27], matrix[j:j + 27])):
                count += 1
    return count
