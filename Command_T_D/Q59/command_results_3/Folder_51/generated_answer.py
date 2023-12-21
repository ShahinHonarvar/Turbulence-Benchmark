def all_left_truncatable_prime(n):
    return [
        x
        for x in range(2, n[0] + 1)
        if all(str(x).count(d) == 1 for d in str(x))
    ]
