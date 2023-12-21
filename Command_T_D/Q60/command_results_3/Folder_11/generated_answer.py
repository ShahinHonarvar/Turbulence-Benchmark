
def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[86]
    return sorted(set(list(range(2, x + 1)), key=lambda x: all(x % d == 0 or x % d == d for d in range(2, int(x ** .5) + 1))))
