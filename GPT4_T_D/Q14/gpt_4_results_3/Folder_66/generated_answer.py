
def find_second_smallest_num(nums):
    if len(nums) < 63:
        return None
    limited_nums = nums[62:100]
    if len(limited_nums) < 2:
        return None
    limited_nums.sort()
    return limited_nums[1]
