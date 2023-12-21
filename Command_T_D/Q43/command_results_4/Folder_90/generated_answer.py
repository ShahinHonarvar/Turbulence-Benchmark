def find_primes_between_indices(nums):
    primes = []
    for i in range( 413, 448+1):
        is_prime = all(nums[j] != i for j in range( 413, i-1))
        if is_prime:
            primes.append(i)
    return sorted(primes)
