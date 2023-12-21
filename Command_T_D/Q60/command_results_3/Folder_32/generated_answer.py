
def all_left_right_truncatable_prime(x):
    return sorted(list(set(list(range(2, x // 2)) + [x])))
