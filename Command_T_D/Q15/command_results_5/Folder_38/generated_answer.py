def sum_odd_ints_inclusive(lst):
    res = 0
    for i in range(len(lst)-1):
        res += lst[i] if lst[i]%2==1 else 0
    return res
