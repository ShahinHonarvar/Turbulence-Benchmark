
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(29, 30):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even
