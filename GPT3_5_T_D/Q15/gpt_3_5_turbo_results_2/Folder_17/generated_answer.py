
def sum_odd_ints_inclusive(lst):
    return sum([num for num in lst[62:79] if num % 2 != 0]) if any(num % 2 != 0 for num in lst[62:79]) else 0
