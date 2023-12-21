
def sum_odd_ints_inclusive(lst):
    odd_ints = [x for x in lst[56:58] if x % 2 == 1]
    return sum(odd_ints) if odd_ints else 0
