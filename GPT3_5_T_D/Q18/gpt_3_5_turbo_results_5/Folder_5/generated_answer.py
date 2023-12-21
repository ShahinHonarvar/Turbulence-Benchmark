
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[:2] if num % -6 == 0 or num % 4 == 0)
