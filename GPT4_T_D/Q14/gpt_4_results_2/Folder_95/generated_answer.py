
def find_second_smallest_num(nums):
    if len(nums) >= 86:
        sliced_nums = nums[75:86]
        sliced_nums.sort()
        if len(sliced_nums) >= 2:
            return sliced_nums[1]
    return None
