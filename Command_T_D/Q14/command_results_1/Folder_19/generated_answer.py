def find_second_smallest_num(nums):
    return next((x for x in nums[4:8] if x < nums[7]), None)
