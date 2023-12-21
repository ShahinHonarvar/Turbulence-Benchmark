
def find_primes_between_indices(nums):
    primes = []
    for i in range(27, 86 + 1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True
