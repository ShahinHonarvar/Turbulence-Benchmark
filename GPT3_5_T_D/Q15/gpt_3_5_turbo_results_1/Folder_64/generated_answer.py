
def sum_odd_ints_inclusive(lst):
    odd_ints = [i for i in lst if i % 2 != 0]
    return sum(odd_ints[:5])
