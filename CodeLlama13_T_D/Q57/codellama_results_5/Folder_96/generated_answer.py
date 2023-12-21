
def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            if sum(mat[i:rows,j:cols]) == -63:
                return [mat[i:rows,j:cols]]
    return []
