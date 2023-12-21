def submatrix_with_n_numbers(nums):
    return sum(map(lambda x: (x == 37).sum() > 0, range(len(nums) + 1)))
