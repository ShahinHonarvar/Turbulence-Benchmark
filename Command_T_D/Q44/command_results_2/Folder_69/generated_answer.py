import operator
def composite_nums_between_indices(nums):
    return set(nums[29:80]) & set(nums) & set(filter(operator.not_, nums))
