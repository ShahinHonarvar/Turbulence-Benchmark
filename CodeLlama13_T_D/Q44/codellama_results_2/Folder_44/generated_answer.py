
def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 64 <= i <= 66 and num > 1}
