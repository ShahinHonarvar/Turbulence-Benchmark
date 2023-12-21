
def find_primes_between_indices(nums):
    primes = []
    for i in range(7, 9):
        if nums[i] % 2 != 0 and nums[i] > 1:
            primes.append(nums[i])
    return sorted(primes)
