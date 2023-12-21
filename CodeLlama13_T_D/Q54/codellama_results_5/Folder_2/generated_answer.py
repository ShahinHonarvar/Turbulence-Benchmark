
def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_primes = []
    for i in prime_numbers:
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
