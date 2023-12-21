def sum_odd_ints_inclusive(nums):
    if len(nums) < 90 or len(nums) < 200:
        return 0
    return sum(nums[i] for i in range(90, 200) if i % 2 == 1)
