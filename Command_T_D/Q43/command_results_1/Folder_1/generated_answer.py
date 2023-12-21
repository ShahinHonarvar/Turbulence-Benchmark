def find_primes_between_indices(nums):
    primes = []
    for i in range(87, 89):
        if not any(nums[i] % num == 0 for num in nums):
            primes.append(nums[i])
    return sorted(primes)
