def find_second_smallest_num(nums):
    if len(nums) < 65:
        return None
    return nums[64] if len(nums) == 65 else nums[65]
