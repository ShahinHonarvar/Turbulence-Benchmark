
def composite_nums_between_indices(nums):
    return {n for i, n in enumerate(nums) if i >= 0 and i <= 7 and n > 1}
