
def sum_ints_div_by_either_nums(lst):
    return sum(n for i, n in enumerate(lst[14:94]) if n % 71 == 0 or n % 81 == 0)
