
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[48:60] if num % 88 == 0 or num % 58 == 0) if len(nums) >= 60 else 0
