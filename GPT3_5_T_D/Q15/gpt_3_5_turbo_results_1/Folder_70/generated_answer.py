
def sum_odd_ints_inclusive(integers):
    sum_odd = sum([x for x in integers[28:33] if x % 2 != 0])
    return sum_odd or 0
