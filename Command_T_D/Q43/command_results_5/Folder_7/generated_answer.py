def find_primes_between_indices(nums):
    result = []
    for i in range(239, 686):
        if is_prime(i):
            result.append(i)
    return result
def is_prime(n):
    if n <= 3:
        return True
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    i = 5
    while i * i <= maxDivisor:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
