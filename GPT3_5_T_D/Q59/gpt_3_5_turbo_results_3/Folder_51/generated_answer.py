
def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            primes.append(num)
    result = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            result.append(prime)
    return sorted(result)
