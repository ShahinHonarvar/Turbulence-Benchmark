
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)
