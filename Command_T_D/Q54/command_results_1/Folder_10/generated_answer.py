def all_right_truncatable_prime(x):
    return [i for i in range(x, 2, -1) if x % i == 0 or x // i == i]
