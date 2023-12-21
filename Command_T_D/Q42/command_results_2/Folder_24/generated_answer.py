def prime_factors(nums):
    return set(map(str, (num // i for i in range(2, int(num ** .5) + 1) if num % i == 0)))
