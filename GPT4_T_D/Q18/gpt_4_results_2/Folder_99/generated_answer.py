
def sum_ints_div_by_either_nums(nums):
    sublist = nums[154:799]
    divisible_nums = [num for num in sublist if num % 275 == 0 or num % 580 == 0]
    return sum(divisible_nums) if divisible_nums else 0
