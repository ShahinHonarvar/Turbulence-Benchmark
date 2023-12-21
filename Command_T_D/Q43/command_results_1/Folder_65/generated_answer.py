def find_primes_between_indices(nums):
    primes = []
    for i in range(76, 92+1):
        if all(nums[i] % r != 0 for r in range(3, int(nums[i**0.5])+1)):
            primes.append(nums[i])
    return sorted(primes)
