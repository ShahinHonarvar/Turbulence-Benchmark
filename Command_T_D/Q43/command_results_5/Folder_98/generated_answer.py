def find_primes_between_indices(nums):
    lst = list(range(1, len(nums) + 1))
    primes = [nums[i] for i in lst if all(nums[i] % x != 0 for x in range(2, int(nums[i] ** .5) + 1))]
    return sorted(primes)
