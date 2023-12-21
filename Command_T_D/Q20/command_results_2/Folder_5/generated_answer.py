def find_n_th_smallest_num(nums):
    sm = sorted(nums)
    return sm[nums.count(sm[4]) - 1]
