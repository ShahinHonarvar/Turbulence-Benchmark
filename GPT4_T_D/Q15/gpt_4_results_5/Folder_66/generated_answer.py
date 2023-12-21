
def sum_odd_ints_inclusive(lst):
    subset = lst[50:55]
    odd_numbers_only = [num for num in subset if num % 2 != 0]
    return sum(odd_numbers_only) if odd_numbers_only else 0
