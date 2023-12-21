
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 16):
        for j in range(len(matrix[0]) - 16):
            if all([sum(row[j:j+17]) == 176 for row in matrix[i:i+17]]):
                count += 1
    return count
