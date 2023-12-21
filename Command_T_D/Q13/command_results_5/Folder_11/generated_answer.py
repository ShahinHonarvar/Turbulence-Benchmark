
def find_second_largest_num(nums):
    return next((x for x in nums[37:51] if x > nums[36]), None)
