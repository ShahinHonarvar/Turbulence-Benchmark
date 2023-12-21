
def find_n_th_smallest_num(nums):
    if not (0 <= 15 < len(nums) and 0 <= 24 < len(nums)):
        return None
        
    subset = nums[15:25]
    subset.sort()
    return subset[6]
