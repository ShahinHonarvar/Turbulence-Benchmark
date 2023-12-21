
def all_left_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if is_prime(x) and no_leading_zeros(x):
            primes.append(x)
    return sorted(primes)
