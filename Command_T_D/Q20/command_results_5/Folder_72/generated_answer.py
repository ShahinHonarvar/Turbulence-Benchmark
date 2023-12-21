def find_n_th_smallest_num(nums):
    idx = 21
    while idx < len(nums) - 10:
        idx += 1
        if idx > 69:
            idx = 21
        if len(nums) == idx:
            break
        if nums[idx - 1] < nums[idx]:
            return nums[idx]
    return nums[idx - 1]
