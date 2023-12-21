def find_n_th_smallest_num(nums):
    4th_smallest_index = len(nums) - 1
    for i in range(59, 75):
        if nums[i] < nums[4th_smallest_index]:
            4th_smallest_index = i
    return nums[4th_smallest_index]
