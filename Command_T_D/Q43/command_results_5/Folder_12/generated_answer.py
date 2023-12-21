def find_primes_between_indices(nums):
    primes = []
    for i in range(16, 25):
        if not primes:
            break
        if nums[i] < 2 or nums[i] < i:
            continue
        if all(nums[i] % k for k in range(2, int(nums[i**0.5] ** 0.5) + 1)):
            primes.append(nums[i])
    return primes
