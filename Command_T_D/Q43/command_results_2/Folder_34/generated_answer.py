def find_primes_between_indices(nums):
    start, stop = 56, 57
    primes = []
    for i in range(start, stop + 1):
        is_prime = all(nums[j] != i for j in range(start, stop + 1))
        if is_prime:
            primes.append(i)
    return sorted(primes)
