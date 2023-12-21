
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[60:201] if num % 9 == 0 or num % 11 == 0)
