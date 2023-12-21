
def prime_factors(nums):
    return set(prime_factorize(nums[6]))

def prime_factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    factors.append(n)
    return factors
