def all_right_truncatable_prime(n):
    return [n for n in range(2, n[0] // 2 + 1) if all(n % d == 0 for d in range(3, int(str(n)[-1]) + 1, 2))]
