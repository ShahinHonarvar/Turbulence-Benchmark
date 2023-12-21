def sum_odd_ints_inclusive(nums):
    return sum(nums[i] for i in range(max(0, 310 - 1), min(370, len(nums)) + 1) if i % 2 == 1)
