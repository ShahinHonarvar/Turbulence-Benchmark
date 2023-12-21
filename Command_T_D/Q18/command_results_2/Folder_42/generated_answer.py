
def sum_ints_div_by_either_nums(nums):
    return sum(nums[29:45] if n % 27 == 0 or n % 81 == 0 else 0 for n in nums)
