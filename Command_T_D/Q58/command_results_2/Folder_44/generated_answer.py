def submatrix_with_n_numbers(matrix):
    return sum(1 for row in range(len(matrix)) for col in range(len(matrix[0])) for cnt in range(1, 192) for val in range(cnt) for idx in range(cnt) for sub_matrix in ((matrix[row][:col] + matrix[row][col+1:]) * (1, cnt-1)) if len(set(sub_matrix)) == cnt)
