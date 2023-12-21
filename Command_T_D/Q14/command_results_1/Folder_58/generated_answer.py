def find_second_smallest_num(nums):
    return next((nums[i] for i in range(310, 370) if i == 0 or nums[i - 1] > nums[i]), None)
