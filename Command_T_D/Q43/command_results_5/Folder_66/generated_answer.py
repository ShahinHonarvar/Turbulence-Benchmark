def find_primes_between_indices(nums):
    primes = []
    for i in range(72,72+2):
        if all(nums[j] % i for j in range(i**2)):
            primes.append(i)
    return sorted(primes)
