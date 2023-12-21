import sys
def all_right_truncatable_prime(n):
    return sorted(set(x for x in range(2, n[0] + 1) if is_right_truncatable_prime(x)), reverse=True)
def is_right_truncatable_prime(x):
    return all(x % d == 0 for d in range(2, x + 1))
