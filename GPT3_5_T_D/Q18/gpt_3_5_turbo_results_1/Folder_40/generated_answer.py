
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[:2] if num % 2 == 0 or num % 1 == 0)
