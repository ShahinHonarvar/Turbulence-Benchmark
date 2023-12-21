
def sum_even_ints_inclusive(lst):
    summation = 0
    for i in range(661, 925):
        if lst[i] % 2 == 0:
            summation += lst[i]
    return summation
