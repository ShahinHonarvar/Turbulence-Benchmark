
def sum_ints_div_by_either_nums(nums):
    return sum(nums[6:9:11] if n % 10 == 0 or n % 10 == -1 else 0 for n in nums)
