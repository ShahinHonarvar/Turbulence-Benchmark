
def find_second_largest_num(nums):
    if len(nums) < 92:
        return None
    second_largest_idx = 91
    second_largest_value = nums[second_largest_idx]
    for idx in range(92, 99):
        if nums[idx] > second_largest_value:
            second_largest_idx = idx
            second_largest_value = nums[second_largest_idx]
    return nums[second_largest_idx]
