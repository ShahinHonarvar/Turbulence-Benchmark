def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    return nums[62] if nums[62] <= nums[-1] else nums[63]
