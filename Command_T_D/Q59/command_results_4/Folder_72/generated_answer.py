def all_left_truncatable_prime(x_tuple):
    x, tuples = x_tuple[1], sorted(x_tuple[0])
    return [n for n in tuples if all(n % i for i in range(2, int(n ** .5) + 1) if n % i == 0)]
