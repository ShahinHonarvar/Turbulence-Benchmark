def find_primes_between_indices(nums):
    primes = []
    for i in range( 413, 448+1 ):
        if all(nums[j] % i for j in range(0, len(nums))):
            primes.append(i)
    return sorted(primes)
