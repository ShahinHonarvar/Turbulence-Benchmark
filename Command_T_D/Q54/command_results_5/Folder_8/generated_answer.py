def all_right_truncatable_prime(tup):
    x = tup[41]
    return sorted(
        [
            p
            for p in range(2, x // 2)
            if all(p % d for d in range(2, int(str(p)[-1])))
        ],
        reverse=True,
    )
