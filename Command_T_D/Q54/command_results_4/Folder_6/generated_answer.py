def all_right_truncatable_prime(n):
    x = n[74]
    return sorted(set(range(2, x // 2 + 1)) - {x} for x in range(x // 2, x // 2 + 1) if x % 2 == 0 and all(x % d == 0 for d in range(3, int(x ** .5) + 1)))
