def all_left_truncatable_prime(n):
    res = []
    for i in range(2, n[0]):
        j = i
        k = i
        while k:
            k //= 10
            if k in (1, 2, 5, 3, 7):
                break
            if not j % k:
                break
            j += 1
        else:
            res.append(i)
    return res
