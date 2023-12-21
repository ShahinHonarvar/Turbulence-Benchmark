
def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(40, 81):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result
