def all_right_truncatable_prime(n):
    x = n[64]
    return sorted(n[:64] + [n[i] for i in range(1, 64) if all(n[i:j] % 10 != d for d in range(10))])
