
def find_primes_between_indices(nums):
    primes = []
    for i in range(27, 86+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
