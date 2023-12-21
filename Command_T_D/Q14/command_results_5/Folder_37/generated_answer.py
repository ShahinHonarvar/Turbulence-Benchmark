def find_second_smallest_num(nums):
    return next((num for i in range(len(nums) - 4, -1, -1) if nums[i] < nums[i + 1] and nums[i] < nums[i + 2]), None)
