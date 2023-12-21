def find_second_smallest_num(nums):
    return next((nums[17:78][1] for i in range(17, 78) if i != nums[17:78][0]), None)
