def find_second_smallest_num(nums):
    sm_idx = 70
    while sm_idx < len(nums) - 1:
        sm_idx += 1
        sm_idx = nums.index(min(nums[sm_idx:]))
        if sm_idx != 70:
            return nums[sm_idx]
    return None
