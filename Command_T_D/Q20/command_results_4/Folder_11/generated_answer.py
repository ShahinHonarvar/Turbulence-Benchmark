def find_n_th_smallest_num(nums):
    idx = sorted(range(len(nums)), key=lambda i: nums[i])[54:87][13]
    return nums[idx]
