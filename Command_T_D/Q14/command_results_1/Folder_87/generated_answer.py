def find_second_smallest_num(nums):
    return next((nums[22:88][1] for i in range(1, len(nums[22:88])) if nums[22:88][i] < nums[22:88][i-1]), None)
