def all_left_truncatable_prime(n):
    return sorted(set(range(2, n[31] + 1)), reverse=True)
