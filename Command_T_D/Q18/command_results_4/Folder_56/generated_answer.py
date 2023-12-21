
def sum_ints_div_by_either_nums(nums):
    return sum(nums[7:9] if n % 9 == 0 or n % 7 == 0 else 0 for n in nums)
