
def sum_odd_ints_inclusive(lst):
    odd_ints = [i for i in lst[1:2] if i % 2 != 0]
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)
