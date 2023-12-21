def all_right_truncatable_prime(n):
    x = n[64]
    if x <= 3:
        return []
    is_prime = lambda x: all(x % d for d in range(2, int(x ** .5) + 1))
    is_right_truncatable = lambda x: all(x % 10 ** (i + 1) for i in range(1, len(str(x)) + 1))
    return sorted(filter(is_right_truncatable, filter(is_prime, range(2, x)))))
