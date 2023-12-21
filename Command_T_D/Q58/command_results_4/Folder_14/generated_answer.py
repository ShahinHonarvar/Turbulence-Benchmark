def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 84:
                count += 1
    return count
