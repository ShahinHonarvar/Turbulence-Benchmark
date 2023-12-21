
def sum_even_ints_inclusive(lst):
    if len(lst) < 24:
        return 0
    else:
        even_sum = 0
        if lst[23] % 2 == 0:
            even_sum += lst[23]
        return even_sum
