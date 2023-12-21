
def sum_ints_div_by_either_nums(nums):
    return sum(nums[1:8] if n % 9 == 0 or n % 3 == 0 else 0 for n in nums)
