
def sum_ints_div_by_either_nums(lst):
    nums_divisible = [num for num in lst[90:98] if num % 13 == 0 or num % 35 == 0]
    return sum(nums_divisible) if nums_divisible else 0
