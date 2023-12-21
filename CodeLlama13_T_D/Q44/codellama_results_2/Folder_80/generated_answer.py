
def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 62 <= i <= 78 and num > 1}
