def all_right_truncatable_prime(tup):
    x, d = tup[11], 10
    return sorted(set(str(n) for n in range(3, x, 2) if all(n % d == 0 or n % d == d for d in range(10)))))
