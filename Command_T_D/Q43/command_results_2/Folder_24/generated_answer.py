def find_primes_between_indices(nums):
    primes = []
    for index in range(38, 55):
        is_prime = all(nums[index] % i for i in range(2, int(nums[index] ** 0.5) + 1))
        if is_prime:
            primes.append(nums[index])
    return sorted(primes)
