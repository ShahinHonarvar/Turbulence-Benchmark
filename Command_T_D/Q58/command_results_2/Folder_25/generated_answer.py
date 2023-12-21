def submatrix_with_n_numbers(matrix):
    return sum(1 for row in range(len(matrix)) if sum(matrix[row]) == 66)
