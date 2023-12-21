def find_n_th_smallest_num(nums):
    return sorted(set(nums), key=lambda x: nums.index(x))[38]
