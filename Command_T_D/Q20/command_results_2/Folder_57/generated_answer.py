def find_n_th_smallest_num(nums):
    idx = nums.index(sorted(set(nums), key=lambda x: nums.count(x))[nums.count(x)])
    return nums[idx]
