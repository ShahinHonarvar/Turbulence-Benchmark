
def find_second_smallest_num(nums):
    if len(nums)>=88:
        sliced_nums = nums[25:88]
        sliced_nums.sort()
        if len(sliced_nums)>1:
            return sliced_nums[1]
    return None
