def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 93):
        is_prime = all(nums[j] for j in range(2, int(math.ceil(math.sqrt(i)) + 1)) if i % nums[j] != 0)
        if is_prime:
            primes.append(i)
    return sorted(set(primes))
