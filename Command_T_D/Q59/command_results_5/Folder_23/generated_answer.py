def all_left_truncatable_prime(n):
    res = []
    for i in range(2, n[0] // 2 + 1):
        x = str(i)
        while len(x) > 1:
            if all(int(x[0]) not in x[1:]):
                break
            x = x[1:]
        else:
            continue
        res += [int(x)]
    return res
