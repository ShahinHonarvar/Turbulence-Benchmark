
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_row = matrix[i][j:]
            current_column = [row[j] for row in matrix]
            current_submatrix = np.array([current_row, current_column])
            if np.sum(current_submatrix) == -37:
                result.append(current_submatrix)
    return result
