def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(6, len(lst), 2):
        result += lst[i]
    return result
