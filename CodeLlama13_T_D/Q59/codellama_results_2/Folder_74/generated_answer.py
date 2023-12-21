
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for x in numbers:
        if str(x).find("0") == -1 and is_prime(x):
            left_truncatable_primes.append(x)
    return sorted(left_truncatable_primes)
