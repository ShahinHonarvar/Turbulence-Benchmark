def composite_nums_between_indices(nums):
    c = set(nums) & set(range(4))
    return c & set(range(1, int(nums[-1] ** 0.5) + 1))
