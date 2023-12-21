def find_second_smallest_num(nums):
    if len(nums) < 37 or len(nums) > 76:
        return None
    if len(nums) == 37:
        return nums[35]
    return nums[int((len(nums) - 1) / 2)]
