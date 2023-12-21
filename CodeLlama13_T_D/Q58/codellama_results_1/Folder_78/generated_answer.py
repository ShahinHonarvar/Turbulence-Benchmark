
def submatrix_with_n_numbers(matrix):
    n = 91
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if all([sum(row[j:j+n]) == n for row in matrix[i:i+n]]):
                count += 1
    return count
