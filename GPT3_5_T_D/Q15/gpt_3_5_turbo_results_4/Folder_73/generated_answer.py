
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[19:93] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
