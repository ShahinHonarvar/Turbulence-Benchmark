
def sum_odd_ints_inclusive(lst):
    return sum(num for i, num in enumerate(lst[:11]) if num % 2 != 0)
