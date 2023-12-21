def find_second_smallest_num(nums):
    return next((nums[22:88][1] for i in range(len(nums[22:88]))) if len(nums[22:88]) >= 2 else None)
