
def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 3 <= i <= 5 and num > 1}
