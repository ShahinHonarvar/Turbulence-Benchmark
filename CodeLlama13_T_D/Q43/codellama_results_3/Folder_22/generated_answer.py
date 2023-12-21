
def find_primes_between_indices(nums):
    primes = []
    for i in range(75, 86):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
