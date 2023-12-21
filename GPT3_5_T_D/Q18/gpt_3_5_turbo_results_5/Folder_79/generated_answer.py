
def sum_ints_div_by_either_nums(nums):
    range_nums = nums[8:10]
    divisible_nums = [num for num in range_nums if num % -3 == 0 or num % 6 == 0]
    return sum(divisible_nums) if divisible_nums else 0
