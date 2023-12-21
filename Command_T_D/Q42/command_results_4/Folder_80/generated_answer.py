import sys
def prime_factors(nums):
    return set(prime_factors_inner(nums[746]))
def prime_factors_inner(num):
    if num < 2:
        return []
    if num == 2 or num == 3:
        return [num]
    factors = []
    for i in range(5, int(num ** .5) + 1):
        if num % i == 0:
            factors.extend(prime_factors_inner(num // i))
            break
    if num > 2:
        factors.extend(prime_factors_inner(num - 1))
    if num > 3:
        factors.extend(prime_factors_inner(num - 2))
    return factors
