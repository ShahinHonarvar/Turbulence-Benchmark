def submatrix_with_particular_sum(nums):
    return [row[:] for row in zip(*[iter(nums)]*nums.shape[1]) if sum(row) == 54]
