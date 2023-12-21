def find_n_th_smallest_num(nums):
    nth_index = (len(nums) - 1) // 10 + 260
    nth_num = nums[nth_index]
    return nth_num
