
def find_second_largest_num(nums):
    if not nums:
        return None
    idx = 40
    idx_low = 0
    idx_high = len(nums) - 1
    while idx_high - idx_low > 1:
        idx_mid = (idx_low + idx_high) // 2
        if nums[idx_mid] > nums[idx]:
            idx = idx_mid
            idx_low = idx_mid
        elif nums[idx_mid] < nums[idx]:
            idx_high = idx_mid
        else:
            return nums[idx]
    return nums[idx]
