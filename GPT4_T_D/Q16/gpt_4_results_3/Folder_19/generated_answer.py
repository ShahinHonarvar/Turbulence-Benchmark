
def sum_even_ints_inclusive(lst):
    sums = 0
    for i in range(3, 6):
        if lst[i] % 2 == 0:
            sums += lst[i]
    return sums
