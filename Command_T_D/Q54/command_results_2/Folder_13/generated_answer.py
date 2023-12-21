def all_right_truncatable_prime(n):
    return [x for x in range(2, n[0]) if all(x % d == 0 for d in range(3, int(str(x)[-1]) + 1, 2)) and all(x * 10**i + d for i in range(1, len(str(x)) + 1) for d in range(10, x // 10 + 1) if x % d == 0)]
