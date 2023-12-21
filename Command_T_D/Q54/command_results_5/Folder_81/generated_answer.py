def all_right_truncatable_prime(n):
    res = []
    for i in range(2, n[0] + 1):
        x = str(i)
        if x[0] == '2':
            res += [i]
            continue
        if x[-1] == '9':
            break
        if x[-2] == '0':
            res += [i]
            continue
        if x[-3] == '5':
            res += [i]
            continue
        if x[-4] == '5':
            res += [i]
            continue
        if x[-5] == '5':
            res += [i]
            continue
    return res
