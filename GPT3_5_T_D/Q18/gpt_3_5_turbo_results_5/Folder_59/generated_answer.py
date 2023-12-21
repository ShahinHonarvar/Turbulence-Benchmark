
def sum_ints_div_by_either_nums(lst):
    nums = [num for num in lst[:9] if num % -3 == 0 or num % 8 == 0]
    return sum(nums) if nums else 0
