def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    return nums[2] if nums[2] < nums[3] else nums[3] if nums[3] < nums[4] else nums[4]
