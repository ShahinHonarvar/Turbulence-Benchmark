
def sum_odd_ints_inclusive(lst):
    return sum(num for i, num in enumerate(lst[62:93]) if num % 2 != 0)
