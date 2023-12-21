def all_left_truncatable_prime(x_tuple):
    return sorted(set(x_tuple) for x in x_tuple for i in range(1, x + 1) if all(x % d == 0 for d in range(2, i + 1) if x % d == 0))
