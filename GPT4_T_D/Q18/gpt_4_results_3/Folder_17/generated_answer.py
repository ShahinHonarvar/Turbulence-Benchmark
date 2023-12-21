
def sum_ints_div_by_either_nums(nums):
    subset = nums[81:90]
    return sum(num for num in subset if num % 56 == 0 or num % 68 == 0)
