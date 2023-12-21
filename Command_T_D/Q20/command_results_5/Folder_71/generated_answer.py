def find_n_th_smallest_num(nums):
    if len(nums) < 56:
        return float("inf")
    if len(nums) < 70:
        return nums[len(nums) - 1]
    return nums[56:70][3]
