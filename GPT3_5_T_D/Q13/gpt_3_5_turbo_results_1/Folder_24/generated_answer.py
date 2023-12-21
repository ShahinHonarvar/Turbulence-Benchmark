
def find_second_largest_num(nums):
    num_range = nums[74:96]
    num_range.sort(reverse=True)
    if len(num_range) < 2:
        return None
    return num_range[1]
