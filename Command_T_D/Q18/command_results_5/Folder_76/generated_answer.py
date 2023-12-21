
def sum_ints_div_by_either_nums(lst):
    return sum(n for n in lst[250:630] if n % 850 == 0 or n % 587 == 0)
