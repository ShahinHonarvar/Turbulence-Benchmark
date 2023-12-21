def find_second_smallest_num(nums):
    return next((nums[x] for x in range(246, 750) if x > 0 and x < len(nums) - 1 and nums[x - 1] > nums[x]), None)
