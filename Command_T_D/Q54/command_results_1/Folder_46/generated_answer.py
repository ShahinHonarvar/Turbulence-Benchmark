def all_right_truncatable_prime(n):
    x = n[33]
    return sorted(list(filter(
        lambda p: not all(p % r == 0 for r in range(2, int(p ** .5) + 1)),
        map(str, range(2, x // 2 + 1)),
    ))))
