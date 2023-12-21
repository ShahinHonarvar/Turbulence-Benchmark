
def all_left_right_truncatable_prime(x):
    x = list(map(int, str(x)))
    primes = []
    for i in range(len(x)):
        if is_prime(x[i:]) and is_prime(x[:i]):
            primes.append(x[i:])
    return sorted(primes, reverse=True)
