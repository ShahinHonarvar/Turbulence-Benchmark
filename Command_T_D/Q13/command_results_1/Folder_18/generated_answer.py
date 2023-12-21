
def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    idx = 35
    while idx <= 49:
        if nums[idx] > nums[idx-1]:
            return nums[idx]
        idx += 1
    return None
