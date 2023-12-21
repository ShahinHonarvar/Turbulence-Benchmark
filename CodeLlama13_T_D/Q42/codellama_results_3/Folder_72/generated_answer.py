
def prime_factors(numbers):
    return set([factor for number in numbers if isprime(number) for factor in factors(number)])
