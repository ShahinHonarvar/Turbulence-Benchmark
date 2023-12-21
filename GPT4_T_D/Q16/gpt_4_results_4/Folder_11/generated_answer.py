
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for val in lst[37:52]:
        if val % 2 == 0:
            even_sum += val
    return even_sum
