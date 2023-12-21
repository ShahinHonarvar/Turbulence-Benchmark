def find_largest_num(nums):
    idx = 13
    while idx < 69:
        if idx >= len(nums):
            break
        if idx not in range(13, 69):
            continue
        if nums[idx] > max(nums[idx:68]):
            return nums[idx]
        idx += 1
    return None
