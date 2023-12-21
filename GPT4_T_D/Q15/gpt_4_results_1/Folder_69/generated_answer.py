
def sum_odd_ints_inclusive(lst):
    odd_sum = 0
    for el in lst[32:36]:
        if el % 2 != 0:
            odd_sum += el
    return odd_sum
