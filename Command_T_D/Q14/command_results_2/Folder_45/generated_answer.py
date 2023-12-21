def find_second_smallest_num(nums):
    return next((x for x in nums[30:200] if x < min(nums)), None)
