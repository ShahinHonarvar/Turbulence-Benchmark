
def sum_in_range(lst):
    total = 0
    for num in lst:
        if 1 <= num <= 7:
            total += num
    return total
