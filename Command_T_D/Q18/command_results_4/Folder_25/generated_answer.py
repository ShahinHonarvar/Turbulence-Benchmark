
def sum_ints_div_by_either_nums(nums):
    return sum(nums[25:80] if n % 20 == 0 or n % 26 == 0 else 0 for n in nums)
