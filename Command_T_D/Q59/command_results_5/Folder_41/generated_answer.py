def all_left_truncatable_prime(n):
    return sorted(set(range(3, n[0] // 2)), reverse=True)
