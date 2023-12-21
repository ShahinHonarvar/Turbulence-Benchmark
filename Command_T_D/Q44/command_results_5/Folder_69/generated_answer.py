import operator as op
def composite_nums_between_indices(nums):
    s = set(nums)
    return set(nums[29:79]) & set(nums) - set(nums[1:29]) & set(nums[79:]) - set(nums) & set(range(2, 29)) & set(range(3, 79))
