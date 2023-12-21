def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 93):
        if i not in nums and all(nums[k] % i != 0 for k in range(31, 93)):
            primes.append(i)
    return sorted(primes)
