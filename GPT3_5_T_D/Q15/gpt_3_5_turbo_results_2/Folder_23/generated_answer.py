
def sum_odd_ints_inclusive(lst):
    summation = 0
    for num in lst[52:72]:
        if num % 2 != 0:
            summation += num
    return summation
