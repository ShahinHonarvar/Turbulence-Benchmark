import operator
def composite_nums_between_indices(nums):
    return set(nums[42:52]) & set(nums) - set(nums[42:52]) & set(nums) & set(nums)
