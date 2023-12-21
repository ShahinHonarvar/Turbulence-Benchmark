def find_second_smallest_num(nums):
    return next((nums[i] for i in range(1, len(nums)) if nums[i] < nums[0]), None)
