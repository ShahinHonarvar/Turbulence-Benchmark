def find_n_th_smallest_num(nums):
    19th_smallest_num = None
    for i in range(len(nums) - 1):
        curr = nums[i]
        while curr < 19th_smallest_num:
            curr += 1
        19th_smallest_num = curr
    return 19th_smallest_num
