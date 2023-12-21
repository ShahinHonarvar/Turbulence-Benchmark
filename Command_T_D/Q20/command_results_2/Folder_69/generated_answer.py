def find_n_th_smallest_num(nums):
    n = 17
    start, end = 39, 91
    nums.sort()
    for i in range(start, end):
        if len(nums) - nums[i] < n:
            break
        n -= 1
    return nums[i]
