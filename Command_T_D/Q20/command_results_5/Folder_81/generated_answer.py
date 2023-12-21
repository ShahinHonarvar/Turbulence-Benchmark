def find_n_th_smallest_num(nums):
    sm_num = sorted(nums)[13]
    return nums[nums.index(sm_num) + 1]
