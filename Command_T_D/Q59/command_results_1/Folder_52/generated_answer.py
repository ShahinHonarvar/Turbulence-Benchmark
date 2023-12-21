def all_left_truncatable_prime(n):
    return sorted((p for p in range(3, n[0] + 1) if all(int(i) > 0 for i in str(p))), reverse=True)
