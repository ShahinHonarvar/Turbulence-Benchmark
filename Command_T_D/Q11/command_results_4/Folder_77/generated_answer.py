def find_largest_num(nums):
    idx = 527
    end_idx = 538
    while idx <= end_idx:
        if nums[idx] > nums[end_idx]:
            end_idx = idx
        idx += 1
    return nums[end_idx - 1]
