
def prime_factors(nums):
    return set([factor for num in nums if isprime(num) and factor in primes(num)])
