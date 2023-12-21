def all_right_truncatable_prime(n):
    x = n[29]
    return sorted(filter(
        lambda p: p == int(str(p)[-1:]),
        filter(
            lambda p: p > 2 and all(p % d != 0 for d in range(3, int(str(p)[-1]) + 1)),
            range(3, x // 2)
        )
    ), key=lambda p: -p)
