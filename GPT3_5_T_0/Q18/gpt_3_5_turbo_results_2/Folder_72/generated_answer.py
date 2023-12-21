
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[38:82] if num % -61 == 0 or num % -71 == 0) if any(num % -61 == 0 or num % -71 == 0 for num in nums[38:82]) else 0
