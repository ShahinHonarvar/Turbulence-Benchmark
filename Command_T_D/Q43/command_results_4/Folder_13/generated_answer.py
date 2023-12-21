def find_primes_between_indices(nums):
    primes = []
    for i in range(415, 647 + 1):
        if all(nums[j] % i for j in range(1, int(nums[0] ** .5) + 1)):
            primes.append(i)
    return sorted(primes)
