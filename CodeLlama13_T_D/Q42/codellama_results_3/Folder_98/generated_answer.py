
def prime_factors(nums):
    return set(prime_factor(nums[4]))

def prime_factor(n):
    if n == 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + prime_factor(n/i)
    return [n]
