
def sum_in_range(lst):
    total = 0
    for num in lst:
        if 60 <= num <= 90:
            total += num
    return total
