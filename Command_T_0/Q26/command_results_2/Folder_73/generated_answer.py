def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if 20 <= nums[i] <= 93)
