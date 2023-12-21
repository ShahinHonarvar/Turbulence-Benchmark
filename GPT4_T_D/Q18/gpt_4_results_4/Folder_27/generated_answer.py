
def sum_ints_div_by_either_nums(lst):
    sum_divisible = sum(num for num in lst[20:36] if num % -36 == 0 or num % -89 == 0)
    return sum_divisible
