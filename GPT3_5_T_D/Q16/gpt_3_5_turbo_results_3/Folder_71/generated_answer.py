
def sum_even_ints_inclusive(lst):
    total = 0
    for num in lst[26:53]:
        if num % 2 == 0:
            total += num
    return total
