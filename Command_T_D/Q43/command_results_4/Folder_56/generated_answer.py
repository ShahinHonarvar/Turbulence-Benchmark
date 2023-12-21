def find_primes_between_indices(nums):
    primes = []
    for i in range(40, 69):
        if all(nums[j] % i for j in range(i**2, len(nums), i)):
            primes.append(i)
    return sorted(primes)
