def submatrix_with_particular_sum(mat):
    # The function should return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 87.
    # If no such submatrix is found, the function should return an empty list.
    result = []
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            cur_sum = 0
            for val in mat[row][col]:
                cur_sum += val
            if cur_sum == 87:
                result += [[row, col]]
    return result
