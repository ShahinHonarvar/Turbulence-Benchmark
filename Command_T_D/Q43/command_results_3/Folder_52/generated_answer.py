def find_primes_between_indices(nums):
    primes = []
    for i in range(33, 60):
        is_prime = all(nums[j] % i for j in range(33, 59))
        if is_prime:
            primes.append(i)
    return sorted(set(primes))
