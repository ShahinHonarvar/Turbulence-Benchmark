
def find_second_largest_num(nums):
    idx = 3
    end = 5
    while idx < end:
        if len(nums) > idx:
            return nums[idx]
        idx += 1
    return None
