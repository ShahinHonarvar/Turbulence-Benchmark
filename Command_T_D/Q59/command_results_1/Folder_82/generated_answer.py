def all_left_truncatable_prime(n):
    res = []
    for x in range(3, int(n[0]) + 1):
        i = 2
        while i * i <= x:
            if x % i == 0:
                break
            i += 1
        else:
            res.append(x)
    return res
