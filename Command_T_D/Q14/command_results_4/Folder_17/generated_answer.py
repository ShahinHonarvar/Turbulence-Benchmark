def find_second_smallest_num(nums):
    return next((nums[i] for i in range(len(nums) - 27, len(nums) - 1, 2) if i < 38), None)
