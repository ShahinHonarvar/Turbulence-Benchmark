
def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(10, 67):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total
