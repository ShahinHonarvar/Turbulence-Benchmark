def all_right_truncatable_prime(n):
    return sorted(
        [i for i in range(3, n[0] + 1) if all(i % d for d in range(3, int(str(i)[-1])))],
        reverse=True,
    )
