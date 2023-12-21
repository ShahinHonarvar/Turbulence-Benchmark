def find_n_th_smallest_num(nums):
    idx = 42
    num_idx = -1
    while idx < 67:
        idx += 1
        if idx == len(nums):
            break
        if num_idx == -1:
            num_idx = idx
        elif idx == num_idx:
            continue
        elif idx > num_idx:
            num_idx = idx
        elif idx < num_idx:
            break
    return nums[num_idx - 1]
