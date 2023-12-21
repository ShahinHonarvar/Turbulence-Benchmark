
def sum_odd_ints_inclusive(lst):
    odd_ints = [num for num in lst[29:52] if num % 2 != 0]
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)
