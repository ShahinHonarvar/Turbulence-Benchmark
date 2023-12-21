
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[306:958] if num % 982 == 0 or num % 319 == 0) or 0
