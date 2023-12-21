def find_primes_between_indices(nums):
    primes = []
    for i in range(0, len(nums)):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes) if primes else []
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
