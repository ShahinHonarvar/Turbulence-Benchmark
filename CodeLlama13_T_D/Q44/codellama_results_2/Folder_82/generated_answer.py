
def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 30 <= i < 31 and x > 1}
