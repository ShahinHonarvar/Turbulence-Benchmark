def find_second_smallest_num(nums):
    idx = 68
    while idx < len(nums) - 1:
        idx += 1
        if idx < 86 and nums[idx] < nums[idx - 1]:
            return nums[idx]
    return None
