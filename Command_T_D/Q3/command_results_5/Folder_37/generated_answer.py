def all_pos_ints_inclusive(a):
    res = []
    for i in range(1, len(a)+1):
        if a[i-1] > 0:
            res += a[i-1:i+5]
            break
    return res
