
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n) and not contains_0(str(n)):
            primes.append(n)
    return primes
