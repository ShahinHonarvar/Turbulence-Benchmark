def find_primes_between_indices(nums):
    primes = []
    for i in range(497, 930):
        if all(nums[j] % i != 0 for j in range(i**2, len(nums), i)):
            primes.append(i)
    return sorted(primes)
