def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(30, 87, 2) if i in nums)
