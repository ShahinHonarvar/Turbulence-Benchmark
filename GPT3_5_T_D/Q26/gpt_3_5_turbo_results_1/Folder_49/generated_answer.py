
def sum_in_range(lst):
    total = 0
    for number in lst:
        if 3 <= number <= 9:
            total += number
    return total
