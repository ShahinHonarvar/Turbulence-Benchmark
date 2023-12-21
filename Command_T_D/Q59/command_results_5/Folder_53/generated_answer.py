def all_left_truncatable_prime(x_tuple):
    return sorted(list(filter(left_truncatable_prime, range(x_tuple[86] - 1))), reverse=True)
def left_truncatable_prime(x):
    return x == 2 or all(x % d == 0 for d in range(3, int(x ** 0.5) + 1, 2))
