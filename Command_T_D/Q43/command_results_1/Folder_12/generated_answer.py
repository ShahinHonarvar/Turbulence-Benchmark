def find_primes_between_indices(nums):
    start = nums[16]
    end = nums[25]
    primes = []
    for i in range(start, end+1):
        is_prime = all(nums[k] * i for k in range(3, int(i**(0.5))+1))
        if is_prime:
            primes.append(i)
    return primes
