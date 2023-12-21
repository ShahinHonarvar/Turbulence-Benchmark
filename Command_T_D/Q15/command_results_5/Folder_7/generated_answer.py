def sum_odd_ints_inclusive(ints):
    return sum(int(n) for n in ints[661::2] if n <= 924)
