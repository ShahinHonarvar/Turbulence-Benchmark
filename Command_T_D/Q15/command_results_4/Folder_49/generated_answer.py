def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(80, 200, 2) if i not in nums)
