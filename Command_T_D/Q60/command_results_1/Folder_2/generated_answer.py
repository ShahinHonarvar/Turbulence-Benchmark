
def all_left_right_truncatable_prime(x_range):
    return sorted(list(set(range(2, x_range[0] + 1, x_range[1] - 1, 2)) for _ in range(10) if _ not in '0123456789')
