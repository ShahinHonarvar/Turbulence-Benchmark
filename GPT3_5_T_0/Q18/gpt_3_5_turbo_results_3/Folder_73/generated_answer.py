
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[81:87] if num % -33 == 0 or num % -62 == 0) or 0
