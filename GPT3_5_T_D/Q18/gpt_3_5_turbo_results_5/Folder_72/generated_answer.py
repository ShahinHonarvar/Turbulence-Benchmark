
def sum_ints_div_by_either_nums(nums):
    nums_range = nums[38:82]
    divisible_nums = [num for num in nums_range if num % -61 == 0 or num % -71 == 0]
    return sum(divisible_nums) if divisible_nums else 0
