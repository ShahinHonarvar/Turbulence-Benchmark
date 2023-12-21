
def sum_even_ints_inclusive(lst):
    start, end = 52, 71
    sum_even = 0
    for i in range(start, end + 1):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even
