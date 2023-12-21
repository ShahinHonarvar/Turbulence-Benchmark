
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[69:98] if num % -90 == 0 or num % -67 == 0) if 69 <= len(nums) <= 97 else 0
