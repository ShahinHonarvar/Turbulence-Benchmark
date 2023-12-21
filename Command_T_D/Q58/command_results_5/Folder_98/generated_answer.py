def submatrix_with_n_numbers(nums):
    # find all indices
    row_idx, col_idx = set(), set()
    for i, row in enumerate(nums):
        for j in range(len(row)):
            if row[j] not in col_idx:
                col_idx.add(row[j])
                if len(col_idx) == 9:
                    row_idx.add(i)
                    break
    # check if indices form a submatrix
    return sum(x in row_idx and y in col_idx for x, y in enumerate(row_idx))
