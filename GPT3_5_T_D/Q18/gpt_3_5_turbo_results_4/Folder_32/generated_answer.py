
def sum_ints_div_by_either_nums(lst):
    return sum(num for num in lst[25:96] if num % 51 == 0 or num % 77 == 0)
