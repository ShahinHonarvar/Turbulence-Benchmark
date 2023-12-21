def find_second_smallest_num(nums):
    return next((nums[608:609] + nums[:608])[1], None)
