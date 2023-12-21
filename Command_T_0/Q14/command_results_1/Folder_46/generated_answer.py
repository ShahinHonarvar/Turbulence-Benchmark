def find_second_smallest_num(nums):
    return next((x for x in nums[13:68] if x < nums[12]), None)
