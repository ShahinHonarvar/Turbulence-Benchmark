def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    if len(nums) == 2:
        return nums[1]
    return nums[91] if nums[91] < nums[92] else nums[93]
