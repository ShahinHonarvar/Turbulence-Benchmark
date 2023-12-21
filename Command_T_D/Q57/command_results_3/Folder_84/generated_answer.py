def submatrix_with_particular_sum(matrix):
    return [[-308] + matrix[row][:matrix[row].count(-308)] for row in range(len(matrix[0]))]
