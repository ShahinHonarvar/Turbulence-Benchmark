def find_n_th_smallest_num(nums):
    sm_nums = sorted(set(nums))
    return sm_nums[len(sm_nums) - (len(sm_nums) - 32) + 14]
