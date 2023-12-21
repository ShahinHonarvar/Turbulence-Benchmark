
def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(661, 925):
        if lst[i] % 2 != 0:
            sum_odd += lst[i]
    return sum_odd
