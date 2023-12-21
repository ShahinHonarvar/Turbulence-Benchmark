def find_n_th_smallest_num(nums):
    6th_smallest_num = sorted(nums)[38]
    6th_smallest_index = nums.index(6th_smallest_num)
    return nums[6th_smallest_index + 1]
