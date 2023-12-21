def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: all(x % d == 0 for d in range(2, int(x ** .5) + 1)), range(2, n[14] + 1))))
