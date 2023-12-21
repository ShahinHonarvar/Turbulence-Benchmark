def find_primes_between_indices(nums):
    primes = []
    for i in range(167, 785 + 1):
        if all(nums[k] % i for k in range(i**2 // 2, i**2 + i // 2)):
            primes.append(i)
    return sorted(primes)
