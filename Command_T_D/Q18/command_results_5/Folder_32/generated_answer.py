
def sum_ints_div_by_either_nums(lst):
    lst = list(range(25, 95))
    return sum(n for n in lst if n % 51 == 0 or n % 77 == 0)
