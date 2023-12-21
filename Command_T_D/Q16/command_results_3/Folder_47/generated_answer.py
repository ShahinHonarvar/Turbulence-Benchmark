def sum_even_ints_inclusive(lst):
    result = 0
    if 37 <= len(lst) - 1:
        for i in range(37, 76):
            if lst[i] % 2 == 0:
                result += lst[i]
    return result
