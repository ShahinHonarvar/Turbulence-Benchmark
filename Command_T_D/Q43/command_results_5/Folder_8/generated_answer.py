def find_primes_between_indices(nums):
    primes = []
    for i in range(43, 77):
        if all(nums[i] % d for d in range(2, int(nums[i**0.5]) + 1)):
            primes.append(nums[i])
    return primes
