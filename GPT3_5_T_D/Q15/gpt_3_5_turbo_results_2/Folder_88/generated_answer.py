
def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(4, 9):
        if lst[i] % 2 != 0:
            total += lst[i]
    return total
