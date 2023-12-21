def find_primes_between_indices(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0]]
    if nums[0] == nums[1]:
        return [nums[0]]
    primes = []
    for x in range(2, nums[1] + 1):
        if all(x % y != 0 for y in range(2, int(x ** .5) + 1)):
            primes.append(x)
    return sorted(primes)
