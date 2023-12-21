def all_right_truncatable_prime(n):
    x = n[86]
    return sorted([str(n) for n in range(x, x // 2, -1) if all(n % d == 0 for d in range(2, int(str(n)[-1])))])
