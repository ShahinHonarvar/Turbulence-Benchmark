def all_right_truncatable_prime(x):
    return sorted(list(filter(lambda n: all(n % 10 ** i for i in range(1, len(str(n)))), range(2, x + 1))))
