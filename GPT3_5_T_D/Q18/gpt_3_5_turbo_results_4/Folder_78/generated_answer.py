
def sum_ints_div_by_either_nums(nums):
    nums = nums[34:70]
    divisible_nums = [num for num in nums if num % 19 == 0 or num % 32 == 0]
    return sum(divisible_nums) if divisible_nums else 0
