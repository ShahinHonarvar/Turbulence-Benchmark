def find_primes_between_indices(nums):
    primes = []
    for i in range(69, 85):
        if all(nums[i] % k for k in range(3, int(nums[i**0.5]) + 1)):
            primes.append(nums[i])
    return sorted(primes)
