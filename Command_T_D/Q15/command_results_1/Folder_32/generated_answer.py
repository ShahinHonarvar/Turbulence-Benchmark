def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    return sum(nums[i] for i in range(21, 97, 2))
