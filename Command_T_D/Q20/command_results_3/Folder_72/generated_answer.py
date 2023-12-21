def find_n_th_smallest_num(nums):
    21, 69 = range(21, min(len(nums) + 10, 69) + 1)
    return sorted(nums)[nums[nums[21]] + 1]
