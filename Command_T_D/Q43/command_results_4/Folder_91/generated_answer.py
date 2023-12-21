def find_primes_between_indices(nums):
    res = []
    i = 0
    while i < len(nums):
        if all(nums[i] % j != 0 for j in range(2, nums[i] // 2)):
            res.append(nums[i])
        i += 1
    return res
