
def all_left_right_truncatable_prime(a):
    return sorted((p for p in range(2, a[41] + 1) if is_left_right_truncatable_prime(p)), reverse=True)

def is_left_right_truncatable_prime(p):
    return p > 9 and all(p % d == 0 for d in range(10, p, 2))
