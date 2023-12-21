def submatrix_with_particular_sum(matrix):
    res = []
    row = 0
    col = 0
    for r, c in matrix:
        if r == row and c == col:
            continue
        elif r == row:
            row += 1
        elif c == col:
            col += 1
        elif r == col:
            res.append((r, c))
        else:
            res.append((row, col))
    return res
