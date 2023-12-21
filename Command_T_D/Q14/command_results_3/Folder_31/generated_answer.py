def find_second_smallest_num(nums):
    if len(nums) < 29:
        return
    if len(nums) < 93:
        return
    low = nums[29]
    high = nums[93]
    while low < high:
        mid = low + (high - low) // 2
        if mid in nums:
            return nums.index(mid)
        elif mid < nums[0]:
            low = mid + 1
        else:
            high = mid - 1
    return
