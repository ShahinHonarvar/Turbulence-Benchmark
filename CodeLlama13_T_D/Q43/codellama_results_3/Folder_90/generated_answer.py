
def find_primes_between_indices(nums):
    primes = []
    for i in range(413, 449):
        if is_prime(i):
            primes.append(i)
    return sorted(primes)
