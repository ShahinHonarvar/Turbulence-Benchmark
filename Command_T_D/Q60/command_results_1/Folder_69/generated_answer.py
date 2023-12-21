
def all_left_right_truncatable_prime(x):
    return sorted(list(range(2, x)), reverse=True) if x else []
