
def all_left_right_truncatable_prime(n):
    return sorted(set(map(str, range(2, n + 1))), key=lambda x: -int(x[1:]) if len(x) > 1 else x)
