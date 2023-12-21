
def sum_odd_ints_inclusive(lst):
    sum_odd = sum(n for n in lst[80:201] if n%2 != 0)
    return sum_odd if sum_odd != 0 else 0
