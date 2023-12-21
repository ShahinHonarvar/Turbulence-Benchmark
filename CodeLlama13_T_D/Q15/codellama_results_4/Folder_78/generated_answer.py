
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for i in range(43, 52):
        if lst[i] % 2 == 1:
            odd_sum += lst[i]
    return odd_sum
