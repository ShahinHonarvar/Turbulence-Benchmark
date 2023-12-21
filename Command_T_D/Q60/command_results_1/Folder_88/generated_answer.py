
def all_left_right_truncatable_prime(x):
    return sorted(list(set(range(2, x // 2)) + range(x // 2, x - 1, 2) + [x]))
