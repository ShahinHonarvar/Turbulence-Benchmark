
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[:11] if num % 2 != 0]
    if odd_ints:
        return sum(odd_ints)
    else:
        return 0
