def find_primes_between_indices(nums):
    primes = [i for i in range(76, 93) if all(nums[i] % j != 0 for j in range(2, int(nums[i**0.5]) + 1))]
    return sorted(set(primes))
