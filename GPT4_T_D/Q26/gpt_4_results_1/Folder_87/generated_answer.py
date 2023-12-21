
def sum_in_range(lst):
    total = 0
    for item in lst:
        if 60 <= item <= 90:
            total += item
    return total
