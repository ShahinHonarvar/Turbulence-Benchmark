
def sum_odd_ints_inclusive(integers):
    odd_ints = [x for x in integers[37:52] if x % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
