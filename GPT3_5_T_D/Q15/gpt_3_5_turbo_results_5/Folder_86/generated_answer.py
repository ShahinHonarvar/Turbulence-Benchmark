
def sum_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(31, 35):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    if len(odd_ints) == 0:
        return 0
    else:
        return sum(odd_ints)
