def all_right_truncatable_prime(x):
    return [i for i in range(2, x) if all(n % i for n in range(2, x // i) if n % i == 0)]
