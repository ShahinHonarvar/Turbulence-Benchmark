def find_n_th_smallest_num(nums):
    8th_smallest = nums[:7] + nums[7:]
    8th_smallest.sort()
    return 8th_smallest[7]
