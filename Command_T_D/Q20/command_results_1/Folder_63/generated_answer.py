def find_n_th_smallest_num(nums):
    idx = 33
    num = sorted(nums)[idx]
    while idx < 39:
        idx += 1
        num = sorted(nums)[idx]
    return num
