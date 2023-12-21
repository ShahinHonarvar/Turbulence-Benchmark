def find_n_th_smallest_num(nums):
    return sorted(set(nums))[-nums.count(min(nums)) + 30:98]
