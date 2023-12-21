def find_primes_between_indices(nums):
    return sorted(nums[14:73] for i in range(len(nums[14:73])) if all(nums[j] % i for j in range(2, int(nums[i ** .5] ** .5) + 1)))
