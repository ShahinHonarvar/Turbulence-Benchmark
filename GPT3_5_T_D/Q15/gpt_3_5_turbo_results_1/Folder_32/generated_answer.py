
def sum_odd_ints_inclusive(integers):
    odd_ints = [x for x in integers[21:98] if x % 2 != 0]
    return sum(odd_ints)
