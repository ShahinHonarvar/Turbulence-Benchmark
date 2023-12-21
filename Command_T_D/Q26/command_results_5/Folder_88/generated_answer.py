def sum_in_range(nums):
    return sum(nums) if all(isinstance(nums[i], int) and 1 <= nums[i] <= 7 for i in range(len(nums))) else 0
