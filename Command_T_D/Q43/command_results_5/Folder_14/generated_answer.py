def find_primes_between_indices(nums):
    primes = []
    for i in range(10, 66 + 1):
        is_prime = all(nums[j] for j in range(2, int(nums[0] ** .5) + 1))
        if is_prime:
            primes.append(i)
    return sorted(primes)
