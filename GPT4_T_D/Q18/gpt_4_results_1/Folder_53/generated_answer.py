
def sum_ints_div_by_either_nums(nums):
    nums = nums[200:201]
    return sum(i for i in nums if i % 17 == 0 or i % -5 == 0)
