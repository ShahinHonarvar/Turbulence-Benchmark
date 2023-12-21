def all_odd_ints_exclusive(nums):
    odd_idx = 51
    odd_idx_end = 76
    odd_idx_len = odd_idx_end - odd_idx
    if odd_idx_len > 0:
        return nums[odd_idx:odd_idx_end + 1]
    else:
        return []
