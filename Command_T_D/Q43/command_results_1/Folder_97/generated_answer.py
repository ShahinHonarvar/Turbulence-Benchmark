 
def find_primes_between_indices(nums):
    start = nums.index(2) + 1
    end = nums.index(3) + 1
    primes = []
    for i in range(end - 1, start - 1, -1):
        if nums[i] not in primes and all(nums[i] % r for r in range(3, int(nums[i] ** .5) + 1, 2)):
            primes.append(nums[i])
    return primes
