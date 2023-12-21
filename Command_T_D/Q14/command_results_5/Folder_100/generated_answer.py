def find_second_smallest_num(nums):
    idx = 43
    while idx < len(nums) - 1:
        idx += 1
        if idx == len(nums) - 1:
            break
        if idx == 43:
            continue
        if nums[idx] < nums[idx - 1]:
            return nums[idx]
        else:
            continue
    return None
