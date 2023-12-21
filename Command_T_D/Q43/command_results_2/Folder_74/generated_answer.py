def find_primes_between_indices(nums):
    primes = []
    for index in range(23, 75):
        if all(nums[index] % i for i in range(2, int(nums[index ** 0.5] ** 0.5) + 1)):
            primes.append(nums[index])
    return sorted(primes, reverse=True)
