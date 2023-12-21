
def sum_odd_ints_inclusive(lst):
    return sum(num for i, num in enumerate(lst[56:67]) if num % 2 != 0) or 0
