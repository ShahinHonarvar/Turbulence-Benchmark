def find_n_th_smallest_num(nums):
    nums.sort()
    return nums[nums.index(nums[2:8]) - 2]
