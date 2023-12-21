
def sum_ints_div_by_either_nums(nums):
    subset = nums[20:94]
    total = sum(num for num in subset if num % -92 == 0 or num % -50 == 0)
    return total
