
def sum_in_range(lst):
    total = 0
    for num in lst:
        if 10 <= num <= 97:
            total += num
    return total
