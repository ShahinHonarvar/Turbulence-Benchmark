
def all_left_right_truncatable_prime(n):
    return sorted(set(range(2, n[23] + 1)) - set(n[23] + 1))
