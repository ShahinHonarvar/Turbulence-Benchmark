def find_second_smallest_num(nums):
    return nums[37:76].index(sorted(nums[37:76])[1]) if len(nums) > 76 else None
