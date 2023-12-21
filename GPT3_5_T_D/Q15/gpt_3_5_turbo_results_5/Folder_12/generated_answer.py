
def sum_odd_ints_inclusive(integers):
    odd_integers = [x for x in integers[14:65] if x % 2 != 0]
    return sum(odd_integers)
