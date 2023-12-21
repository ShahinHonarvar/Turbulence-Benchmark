def find_n_th_smallest_num(nums):
    return sorted(nums)[len(nums)-nums.count(sorted(nums)[2])-2]
