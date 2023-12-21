
def find_n_th_smallest_num(nums):
    if len(nums) >= 72:
        nums_range = sorted(nums[16:72])
        if len(nums_range) >= 14:
            return nums_range[13]
    return "Invalid Input"
