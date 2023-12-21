def find_largest_num(nums):
    idx = 527
    largest = nums[idx]
    while idx < 538:
        idx += 1
        largest = max(largest, nums[idx])
    return largest
