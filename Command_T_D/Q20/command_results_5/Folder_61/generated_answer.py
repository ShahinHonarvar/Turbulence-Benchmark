def find_n_th_smallest_num(nums):
    return sorted(set(nums))[nums.index(sorted(set(nums))[9]) - 1]
