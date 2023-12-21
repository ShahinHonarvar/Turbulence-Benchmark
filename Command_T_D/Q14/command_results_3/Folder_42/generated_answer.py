def find_second_smallest_num(nums):
    return next((x for x in nums[20:98] if x < nums[20]), None)
