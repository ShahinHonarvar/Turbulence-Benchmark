def all_left_truncatable_prime(n):
    return sorted(list(range(2, n[0] // 2)), reverse=True)
