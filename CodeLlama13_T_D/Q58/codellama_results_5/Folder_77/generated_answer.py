
def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 179:
                count += 1
    return count
