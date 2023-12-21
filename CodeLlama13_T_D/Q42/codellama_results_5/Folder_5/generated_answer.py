
def prime_factors(numbers):
    return set([factor for num in numbers if isprime(num) for factor in factors(num)])
