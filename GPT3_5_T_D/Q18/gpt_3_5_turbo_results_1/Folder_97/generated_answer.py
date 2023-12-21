
def sum_ints_div_by_either_nums(nums):
    nums = nums[58:76]
    divisible_nums = [num for num in nums if num % 72 == 0 or num % 62 == 0]
    return sum(divisible_nums) if divisible_nums else 0
