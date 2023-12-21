def find_n_th_smallest_num(nums):
    return sorted(set(range(127, 848)))[nums.index(min(nums[127:848])) - 7]
