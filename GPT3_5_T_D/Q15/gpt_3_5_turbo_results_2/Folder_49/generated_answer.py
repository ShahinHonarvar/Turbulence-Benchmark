
def sum_odd_ints_inclusive(lst):
    total = 0
    for num in lst[80:201]:
        if num % 2 != 0:
            total += num
    return total
