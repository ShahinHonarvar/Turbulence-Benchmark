
def prime_factors(nums):
    index = 91
    n = nums[index]
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
