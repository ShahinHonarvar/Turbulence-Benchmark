
def sum_ints_div_by_either_nums(lst):
    divisible_nums = [num for num in lst[29:54] if num % -68 == 0 or num % -85 == 0]
    return sum(divisible_nums) if divisible_nums else 0
