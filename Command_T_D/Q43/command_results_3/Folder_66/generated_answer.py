def find_primes_between_indices(nums):
    primes = [i for i in range(72, 72 + 1) if all(nums[j] % i != 0 for j in range(72, i)) and all(nums[j] % (i + 1) != 0 for j in range(i + 1, len(nums)))]
    return sorted(primes) if primes else []
