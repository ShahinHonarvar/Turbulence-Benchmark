def submatrix_with_n_numbers(matrix):
    return sum(1 for r in range(1, len(matrix) + 1) for c in range(1, len(matrix[0]) + 1) if matrix[r - 1][c - 1] == 48)
