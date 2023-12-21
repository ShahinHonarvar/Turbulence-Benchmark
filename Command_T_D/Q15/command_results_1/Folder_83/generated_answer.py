def sum_odd_ints_inclusive(ints):
    return sum(i for i in range(ints.index(90), ints.index(200) + 1) if i % 2)
