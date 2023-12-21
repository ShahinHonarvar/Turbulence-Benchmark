
def all_right_truncatable_prime(numbers):
    x = numbers[85]
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_numbers.append(i)
    right_truncatable_primes = []
    for prime in prime_numbers:
        right_truncatable_prime = True
        for i in range(2, len(str(prime))):
            if not is_prime(int(str(prime)[0:-i])):
                right_truncatable_prime = False
                break
        if right_truncatable_prime:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)
