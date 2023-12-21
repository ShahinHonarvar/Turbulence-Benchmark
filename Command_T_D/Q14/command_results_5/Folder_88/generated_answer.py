def find_second_smallest_num(nums):
    return next((x for x in nums[5:-2] if x <= nums[7]), None)
