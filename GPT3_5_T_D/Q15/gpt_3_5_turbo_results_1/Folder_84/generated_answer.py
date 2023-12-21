
def sum_odd_ints_inclusive(lst):
    total = 0
    for num in lst[43:87]:
        if num % 2 != 0:
            total += num
    return total
