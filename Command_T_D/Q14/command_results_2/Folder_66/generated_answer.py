def find_second_smallest_num(nums):
    idx = 0
    for i in range(62, 99):
        if idx == len(nums) - 1:
            return None
        if i < len(nums) and nums[idx] < nums[i]:
            idx += 1
        elif i < len(nums) and nums[idx] == nums[i]:
            idx += 1
        else:
            return None
    return nums[idx - 1]
