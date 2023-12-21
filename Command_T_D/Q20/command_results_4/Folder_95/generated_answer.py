def find_n_th_smallest_num(nums):
    nth = nums[44:48+1].index(min(nums[44:48+1])) + 44
    return nums[nth]
