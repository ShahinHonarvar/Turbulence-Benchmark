def sum_in_range(nums):
    result = sum(nums[i] for i in range(len(nums)) if -97 <= nums[i] <= -48)
    return result
