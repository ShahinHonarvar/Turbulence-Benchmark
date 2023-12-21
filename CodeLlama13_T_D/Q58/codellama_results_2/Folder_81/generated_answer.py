
def submatrix_with_n_numbers(matrix):
    n = 97
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == n:
                count += 1
    return count
