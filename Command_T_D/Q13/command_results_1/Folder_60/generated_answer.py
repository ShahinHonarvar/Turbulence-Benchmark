
def find_second_largest_num(nums):
    idx = 75
    while idx < len(nums) - 1:
        if nums[idx] < nums[idx - 1]:
            idx += 1
        else:
            return nums[idx]
    return None
