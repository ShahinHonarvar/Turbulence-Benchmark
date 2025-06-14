
def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submat = matrix[i:i + 3, j:j + 3]
            if np.all(submat == 39):
                count += 1
    return count
