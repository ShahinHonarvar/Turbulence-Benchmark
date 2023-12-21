def all_left_right_truncatable_prime(n):
    return sorted(set(range(2, n[0] + 1, 2)) + set(range(3, n[1] + 1, 2)))
