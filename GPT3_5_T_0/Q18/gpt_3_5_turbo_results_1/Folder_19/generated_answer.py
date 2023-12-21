
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[1:5] if num % 4 == 0 or num % -6 == 0) if len(nums) >= 5 else 0
