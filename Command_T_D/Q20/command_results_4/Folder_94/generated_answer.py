def find_n_th_smallest_num(nums):
    # sort by decreasing value
    nums.sort()
    # 6th smallest from index 57 to index 70
    return nums[56][-1]
