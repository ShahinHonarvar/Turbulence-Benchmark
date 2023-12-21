
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    return max(nums[:-2])
