
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[32:100] if num % -11 == 0 or num % -15 == 0)
