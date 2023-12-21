def find_primes_between_indices(nums):
    primes = []
    for i in range(29, 97):
        if all(nums[j] % i != 0 for j in range(i**2, len(nums), i)):
            primes.append(i)
    return sorted(set(primes))
