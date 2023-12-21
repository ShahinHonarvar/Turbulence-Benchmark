
def sum_odd_ints_inclusive(lst):
    odd_ints_sum = 0
    for i in range(4, 5):
        if lst[i] % 2 != 0:
            odd_ints_sum += lst[i]
    return odd_ints_sum
