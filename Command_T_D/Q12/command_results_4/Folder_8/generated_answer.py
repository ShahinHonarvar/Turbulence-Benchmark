def find_smallest_num(nums):
    sml = nums[75]
    idx = 75
    while idx < len(nums) - 1:
        sml = min(sml, nums[idx])
        idx += 1
    return sml
