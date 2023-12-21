
def find_second_largest_num(nums):
    a, b = max(nums[:17]), max(nums[17:78])
    if b == a:
        return None
    return b
