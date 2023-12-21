def find_n_th_smallest_num(nums):
    s = sorted(set(nums), key=lambda x: x)
    return s[nums.index(s[52]) + 10]
