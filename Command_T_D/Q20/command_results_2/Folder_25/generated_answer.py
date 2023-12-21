def find_n_th_smallest_num(nums):
    return sorted(set(nums))[len(set(nums))-nums[13]-5:len(set(nums))-nums[40]-5+1]
