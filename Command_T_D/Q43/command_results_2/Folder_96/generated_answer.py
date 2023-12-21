def find_primes_between_indices(nums):
    primes = []
    for i in range(31, 67):
        if i == 2 or i == 3:
            continue
        elif all(nums[i] % k != 0 for k in range(2, int(nums[i] ** 0.5) + 1)):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
