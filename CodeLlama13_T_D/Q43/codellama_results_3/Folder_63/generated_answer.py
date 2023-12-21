
def find_primes_between_indices(nums):
    primes = []
    for i in range(28, 36+1):
        if nums[i-1] % 2 == 0 and nums[i-1] > 1:
            primes.append(nums[i-1])
    return sorted(primes)
