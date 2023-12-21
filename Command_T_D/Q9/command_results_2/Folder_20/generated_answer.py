def all_odd_ints_inclusive(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            res += lst[i]
            break
    return res
