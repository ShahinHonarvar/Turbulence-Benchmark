def find_n_th_smallest_num(nums):
    idx = 85
    while idx < len(nums) - 1:
        idx += 1
        if idx == len(nums) - 1:
            return nums[idx - 1]
        elif idx == 7:
            return nums[idx - 1]
        elif idx == 9:
            return nums[idx - 1]
        elif idx == 99:
            return nums[idx - 1]
