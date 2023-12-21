
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[7:8] if num % 5 == 0 or num % 7 == 0) if any(num % 5 == 0 or num % 7 == 0 for num in nums[7:8]) else 0
