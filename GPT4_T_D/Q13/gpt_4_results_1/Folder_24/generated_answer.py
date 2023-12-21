
def find_second_largest_num(nums):
    if len(nums) < 96:
        return None
    else:
        specific_nums = nums[74:96]
        specific_nums.sort()
        if len(specific_nums) < 2:
            return None
        else:
            return specific_nums[-2]
