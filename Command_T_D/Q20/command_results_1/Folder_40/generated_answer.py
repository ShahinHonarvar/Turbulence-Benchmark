def find_n_th_smallest_num(nums):
    return sorted(set(nums))[4 - nums.index(min(nums))]
