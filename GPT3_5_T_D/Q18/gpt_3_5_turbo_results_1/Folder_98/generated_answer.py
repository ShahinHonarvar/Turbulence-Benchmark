
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[:6] if num % -1 == 0 or num % 13 == 0)
