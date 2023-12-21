def sum_odd_ints_inclusive(lst):
    result = 0
    if lst:
        for i in range(len(lst)):
            result += lst[i] if lst[i] % 2 else 0
    return result
