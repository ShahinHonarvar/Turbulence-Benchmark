
def find_primes_between_indices(nums):
    primes = []
    for i in range(46, 62):
        if nums[i] not in primes:
            primes.append(nums[i])
    return sorted(primes)
