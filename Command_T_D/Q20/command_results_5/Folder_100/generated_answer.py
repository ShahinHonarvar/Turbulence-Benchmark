def find_n_th_smallest_num(nums):
    return sorted(nums)[nums.index(sorted(nums)[11]) - 1]
