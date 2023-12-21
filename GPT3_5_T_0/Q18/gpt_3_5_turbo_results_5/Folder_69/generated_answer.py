
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[61:89] if num % 31 == 0 or num % 11 == 0)
