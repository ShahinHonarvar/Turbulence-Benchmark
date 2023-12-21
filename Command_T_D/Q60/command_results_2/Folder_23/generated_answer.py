
def all_left_right_truncatable_prime(x):
    return sorted(list(range(2, x // 2 + 1)), key=lambda x: str(x))
