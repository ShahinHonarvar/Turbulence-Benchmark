def submatrix_with_n_numbers(matrix):
    return sum(
        0 < i < j < len(matrix) for i in range(0, len(matrix) - 1) for j in range(0, len(matrix[0]) - 1)
    )
