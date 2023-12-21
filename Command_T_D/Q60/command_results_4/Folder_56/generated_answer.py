
def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[30]
    primes = []
    for n in range(2, x + 1):
        if all(n % r for r in range(3, int(str(n)[-1]))) and str(n) in str(num_tuple[0]):
            primes.append(n)
    return primes
