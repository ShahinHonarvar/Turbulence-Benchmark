
def all_left_right_truncatable_prime(n):
    x = n[70]
    return sorted(set(range(2, x // 2 + 1, 2)))
