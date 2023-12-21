def all_right_truncatable_prime(n):
    x = n[32]
    return sorted(
        filter(
            lambda x: all(
                str(x)[:-1] * d + str(x)[-1] in str(x)
                for d in range(2, int(str(x)[-1]) + 1)
            ),
            filter(lambda x: x < x and all(str(x) * d == str(x) for d in range(2, int(str(x)) + 1)),
            range(2, x // 2 + 1),
        ),
    )
