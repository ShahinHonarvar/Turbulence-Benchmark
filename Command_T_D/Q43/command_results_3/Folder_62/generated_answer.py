def find_primes_between_indices(nums):
    primes = []
    for i in range(29, 97):
        if i * i <= len(nums) and all(nums[i * i] % a == 0 for a in range(3, int(nums[i * i] ** .5) + 1)):
            continue
        primes.append(nums[i])
    return primes
