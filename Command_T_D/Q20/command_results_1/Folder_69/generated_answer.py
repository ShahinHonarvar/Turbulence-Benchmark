def find_n_th_smallest_num(nums):
    idx_start = 39
    idx_end = 91
    idx_step = 1
    idx_17 = idx_start + idx_step * 17
    idx_nums = idx_end - idx_start + 1
    idx_pos = idx_nums - idx_17 - 1
    return nums[idx_pos]
