
def find_n_th_smallest_num(nums):
    sliced_nums = nums[106:255]
    sliced_nums.sort()
    return sliced_nums[8]
