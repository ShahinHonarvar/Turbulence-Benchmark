
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[250:630] if num % 850 == 0 or num % 587 == 0)
