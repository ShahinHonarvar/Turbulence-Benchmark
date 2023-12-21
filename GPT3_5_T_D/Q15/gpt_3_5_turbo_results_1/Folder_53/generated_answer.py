
def sum_odd_ints_inclusive(lst):
    summation = 0
    for num in lst[300:301]:
        if num % 2 != 0:
            summation += num
    return summation
