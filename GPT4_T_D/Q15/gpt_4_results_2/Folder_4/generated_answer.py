
def sum_odd_ints_inclusive(lst):
    sum_odd = sum(num for num in lst[12:93] if num % 2 != 0)
    return sum_odd
