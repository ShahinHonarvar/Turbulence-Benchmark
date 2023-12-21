def sum_odd_ints_inclusive(lst):
    result = 0
    for i in range(len(lst) - 2):
        if lst[i] % 2 == 1:
            result += lst[i]
        if lst[i + 1] % 2 == 1:
            result += lst[i + 1]
    if lst[len(lst) - 1] % 2 == 1:
        result += lst[len(lst) - 1]
    return result
