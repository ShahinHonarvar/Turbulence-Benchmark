
def sum_odd_ints_inclusive(lst):
    total = 0
    for num in lst[4:9]:
        if num % 2 != 0:
            total += num
    return total
