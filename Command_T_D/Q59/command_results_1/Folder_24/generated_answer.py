def all_left_truncatable_prime(a):
    for n in range(a[64], 2, -1):
        p = str(n)
        if all(int(p[0] + i) for i in range(1, len(p))):
            yield n
    return
