def find_n_th_smallest_num(nums):
    sm = sorted(set(nums))
    return sm[nums.index(min(sm[34:94])) - 34]
