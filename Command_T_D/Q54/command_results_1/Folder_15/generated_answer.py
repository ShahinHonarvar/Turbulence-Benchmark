def all_right_truncatable_prime(n):
    return sorted(filter(
        lambda x: x > 1 and all(x % d for d in range(2, int(x ** .5) + 1)),
        map(str, range(3, n[6] + 1))
    ), reverse=True)
