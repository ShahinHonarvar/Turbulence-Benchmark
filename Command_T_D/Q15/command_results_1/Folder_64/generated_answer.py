def sum_odd_ints_inclusive(lst):
    result = 0
    for i in range(len(lst) // 2):
        result += lst[i]
    return result
