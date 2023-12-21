
def sum_even_ints_inclusive(lst):
    total = 0
    for num in lst[60:201]:
        if num % 2 == 0:
            total += num
    return total
