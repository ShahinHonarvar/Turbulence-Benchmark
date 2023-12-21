def find_second_smallest_num(nums):
    sml = min(nums)
    idx = 29
    while idx <= 93:
        idx += 1
        if idx > len(nums):
            break
        if nums[idx] < sml:
            return nums[idx]
        elif nums[idx] == sml:
            return nums[idx]
        sml = nums[idx]
    return None
