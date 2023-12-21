def find_primes_between_indices(nums):
    return sorted(list(filter(prime, nums[11:11+11])))
def prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    maxDivisor = x**(0.5)
    for i in range(5, maxDivisor + 1):
        if x % i == 0:
            return False
    return True
