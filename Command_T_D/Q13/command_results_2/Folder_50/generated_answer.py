
def find_second_largest_num(nums):
    idx = 70
    while idx < len(nums) and idx < 84:
        if nums[idx] > nums[idx-1]:
            return nums[idx]
        idx += 1
    return None
