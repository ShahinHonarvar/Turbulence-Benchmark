
def sum_odd_ints_inclusive(lst):
    odd_inds = [i for i in range(68, 87) if lst[i] % 2 == 1]
    return sum(lst[i] for i in odd_inds) or 0
