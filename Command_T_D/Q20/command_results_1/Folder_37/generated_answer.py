def find_n_th_smallest_num(nums):
    return sorted(nums)[5][nums.count(sorted(nums)[5]) - 5]
