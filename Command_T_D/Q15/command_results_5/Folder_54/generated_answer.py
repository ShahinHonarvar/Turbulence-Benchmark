def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(len(nums)-1, len(nums)-34, -2) if nums[i]&1)
