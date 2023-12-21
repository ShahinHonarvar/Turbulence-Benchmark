def find_second_smallest_num(nums):
    return nums[6:8].index(min(nums[6:8])) if len(nums) >= 7 else None
