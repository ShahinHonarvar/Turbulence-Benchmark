
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[69:71] if num % 72 == 0 or num % 70 == 0) if len(nums) >= 71 else 0
