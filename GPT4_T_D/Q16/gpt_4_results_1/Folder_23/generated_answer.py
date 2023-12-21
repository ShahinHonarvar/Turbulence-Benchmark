
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(52, 72):
        try:
            if lst[i] % 2 == 0:
                sum_even += lst[i]
        except IndexError:
            break
    return sum_even
