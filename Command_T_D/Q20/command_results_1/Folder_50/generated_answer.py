def find_n_th_smallest_num(nums):
    idx = 46
    num = float('inf')
    while idx < 83:
        if nums[idx] < num:
            num = nums[idx]
        idx += 1
    return num
