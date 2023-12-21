
def composite_nums_between_indices(nums):
    indices = list(range(28, 41))
    return {num for i, num in enumerate(nums) if i in indices and num > 1}
