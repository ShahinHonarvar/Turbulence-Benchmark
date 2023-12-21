def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(60, 200):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result
