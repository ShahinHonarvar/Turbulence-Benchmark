
def sum_odd_ints_inclusive(lst):
    return sum(num for num in lst[1:2] if num % 2 != 0)
