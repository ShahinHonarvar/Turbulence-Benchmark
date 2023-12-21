
def all_left_right_truncatable_prime(x):
    x = sorted([int(i) for i in str(x)], reverse=True)
    primes = []
    for i in range(len(x)):
        if is_prime(x[i]):
            primes.append(x[i])
    return primes
