def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    for i in range(43, 86, 2):
        if i in nums:
            yield nums[i]
    return sum(nums[i] for i in range(43, 86, 2))
