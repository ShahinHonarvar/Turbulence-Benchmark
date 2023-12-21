def all_right_truncatable_prime(x):
    x -= 1
    return [y for y in range(2, x) if all(y % d for d in range(3, int(str(y)[-1]) + 1, 2)) and all(y % d == 0 or isprime(y - d) for d in range(3, int(str(y)[-1]) + 1, 2))]
