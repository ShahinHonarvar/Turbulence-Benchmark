def find_n_th_smallest_num(nums):
    n = len(nums) - 1
    return sorted(nums)[n - 10]
