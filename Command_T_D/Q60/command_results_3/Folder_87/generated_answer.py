
def all_left_right_truncatable_prime(x):
    return sorted(set(range(2, x + 1)), key=lambda x: str(x))
