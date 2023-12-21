def find_primes_between_indices(nums):
    lst = sorted(range(11, 41))
    for idx in lst:
        if nums[idx] == 2 or nums[idx] == 3:
            continue
        elif nums[idx] < 2 or nums[idx] > 3:
            return []
        elif all(nums[idx] % i != 0 for i in range(2, int(nums[idx] ** .5) + 1)):
            return [nums[idx]]
    return []
