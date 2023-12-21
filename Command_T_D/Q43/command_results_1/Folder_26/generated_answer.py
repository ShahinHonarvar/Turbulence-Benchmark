def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 49):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        maxDivisor = n**0.5
        i = 5
        while i * i <= maxDivisor:
            if n % i == 0:
                return False
            i += 6
        return True
