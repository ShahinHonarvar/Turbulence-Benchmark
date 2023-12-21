def find_second_smallest_num(nums):
    if len(nums) < 31:
        return None
    return nums[31] if nums[31] < nums[32] else nums[32] if nums[32] < nums[33] else nums[33]
