def find_n_th_smallest_num(nums):
    sm = sorted(set(nums))
    return sm[len(sm)-4]
