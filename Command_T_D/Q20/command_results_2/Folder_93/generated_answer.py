def find_n_th_smallest_num(nums):
    6th_smallest_num = nums[40:99] + nums[:40] + nums[99:][::-1] + nums[100:]
    6th_smallest_num.sort()
    return 6th_smallest_num[5]
