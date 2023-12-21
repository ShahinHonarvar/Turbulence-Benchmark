
def all_right_truncatable_prime(numbers):
    x = numbers[81]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    truncatable_primes = []
    for p in prime_numbers:
        if is_truncatable_prime(p):
            truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)
