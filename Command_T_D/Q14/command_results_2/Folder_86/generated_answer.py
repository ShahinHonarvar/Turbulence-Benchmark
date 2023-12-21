def find_second_smallest_num(nums):
    return next((y for x in range(33, 36) for y in nums[x:]), None)
