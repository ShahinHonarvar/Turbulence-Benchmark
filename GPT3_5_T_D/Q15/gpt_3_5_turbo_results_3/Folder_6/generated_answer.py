
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[10:67] if num % 2 != 0]
    return sum(odd_ints)
