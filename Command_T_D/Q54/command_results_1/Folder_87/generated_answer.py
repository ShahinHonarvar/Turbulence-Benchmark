def all_right_truncatable_prime(n):
    x = n[39]
    return sorted((n for n in range(3, int(str(x)[-1]) + 1) if all(n % d for d in range(3, int(str(n)[-1]) + 1, 2)))), reverse=True)
