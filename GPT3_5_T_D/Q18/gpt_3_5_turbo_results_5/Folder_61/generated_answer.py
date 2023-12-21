
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[:7] if num % -5 == 0 or num % -6 == 0)
