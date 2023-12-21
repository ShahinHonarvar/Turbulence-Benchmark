def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 75):
        is_prime = all(nums[j] != i for j in range(2, int(math.ceil(math.sqrt(i)) + 1)) )
        if is_prime:
            primes.append(i)
    return sorted(primes)[::-1]
