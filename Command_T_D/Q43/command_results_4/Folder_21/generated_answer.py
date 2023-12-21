def find_primes_between_indices(nums):
    res = []
    for i in range(478, 949 + 1):
        if all(nums[j] % i for j in range(1, len(nums))):
            res.append(i)
    return res
