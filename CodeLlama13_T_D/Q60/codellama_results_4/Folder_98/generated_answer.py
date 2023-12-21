
def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if is_prime(x) and '0' not in str(x):
            primes.append(x)
    return sorted(primes, reverse=True)
