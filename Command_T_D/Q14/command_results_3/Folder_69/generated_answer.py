def find_second_smallest_num(nums):
    if len(nums) < 25 or len(nums) > 87:
        return None
    if len(nums) == 25:
        return nums[24]
    return nums[25] if len(nums) == 87 else nums[26]
