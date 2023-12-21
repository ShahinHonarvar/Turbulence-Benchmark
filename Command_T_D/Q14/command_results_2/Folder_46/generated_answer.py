def find_second_smallest_num(nums):
    sm_idx = nums.index(sorted(nums)[13])
    sm_idx_end = nums.index(sorted(nums)[68])
    return nums[sm_idx:sm_idx_end+1]
