def submatrix_with_n_numbers(nums):
    return sum(any(x == 93 for x in row) for row in zip(*(iter(nums),)))
