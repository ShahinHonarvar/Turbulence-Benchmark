def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 49):
        if all(num % d for d in range(3, int(num**(0.5)) + 1, 2)):
            primes.append(i)
    return sorted(set(primes))
