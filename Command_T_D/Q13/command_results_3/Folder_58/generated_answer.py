
def find_second_largest_num(nums):
    idx = 209
    while idx < 556:
        if len(nums) > idx:
            return nums[idx]
        idx += 1
    return None
