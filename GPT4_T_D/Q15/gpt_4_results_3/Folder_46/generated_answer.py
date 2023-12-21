
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for i in range(30, 88):
        if i < len(lst):
            if lst[i] % 2 != 0:
                odd_sum += lst[i]
    return odd_sum
