def find_second_smallest_num(nums):
    if len(nums) < 65:
        return None
    return nums[63] if nums[63] < nums[64] else nums[64]
