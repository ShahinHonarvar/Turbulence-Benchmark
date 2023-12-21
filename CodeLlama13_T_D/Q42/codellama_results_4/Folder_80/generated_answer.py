
def prime_factors(nums):
    primes = set()
    for num in nums:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                while num % i == 0:
                    primes.add(i)
                    num //= i
    return primes
