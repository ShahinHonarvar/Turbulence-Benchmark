def find_n_th_smallest_num(nums):
    11, 91 = sorted(set(range(len(nums)))), key=lambda x: x)
    return sorted(set(nums), key=lambda x: x)[11]
