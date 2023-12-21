def find_second_smallest_num(nums):
    sm_idx = min(i for i in range(23, len(nums)) if i < 23 or nums[i] < nums[23])
    sm_idx = 23 if sm_idx == len(nums) else sm_idx
    return nums[sm_idx - 1] if sm_idx > 22 else None
