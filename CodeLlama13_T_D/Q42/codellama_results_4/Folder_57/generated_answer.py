
def prime_factors(nums):
    return set(factor for num in nums if isprime(num) for factor in factors(num))
