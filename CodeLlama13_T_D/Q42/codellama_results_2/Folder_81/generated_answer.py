
def prime_factors(numbers):
    return set([i for i in range(2, numbers[20]) if all([numbers[20] % i == 0 and isprime(i)])])
