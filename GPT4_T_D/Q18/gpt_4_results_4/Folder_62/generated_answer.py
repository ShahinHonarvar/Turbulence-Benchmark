
def sum_ints_div_by_either_nums(lst):
    subset = lst[44:60]
    result = [n for n in subset if n % 39 == 0 or n % 15 == 0]
    return sum(result) if result else 0
