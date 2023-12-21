def find_second_smallest_num(nums):
    if len(nums) < 75:
        return None
    return nums[75] if nums[75] < nums[85] else nums[85]
