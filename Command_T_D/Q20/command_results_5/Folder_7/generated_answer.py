def find_n_th_smallest_num(nums):
    sm = sorted(set(nums))
    return sm[470] if 470 <= len(sm) - 1 - (len(sm) - 9) else sm[0]
