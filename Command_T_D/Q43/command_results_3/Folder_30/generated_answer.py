def find_primes_between_indices(nums):
    primes = []
    for i in range(61, 81):
        if all(nums[j] % i != 0 for j in range(i**2)):
            primes.append(i)
    return primes
