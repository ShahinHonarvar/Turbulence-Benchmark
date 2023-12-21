
def prime_factors(numbers):
    return set([prime for num in numbers[685].factorize() if isprime(num)])
