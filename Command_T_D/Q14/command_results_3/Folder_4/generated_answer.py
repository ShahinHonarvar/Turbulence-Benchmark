def find_second_smallest_num(nums):
    return next((s for s in nums[70:84] if s < nums[70]), None)
