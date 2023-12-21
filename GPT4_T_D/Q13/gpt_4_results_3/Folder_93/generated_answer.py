
def find_second_largest_num(nums):
    if len(nums[75:95]) < 2:
        return None
    else:
        nums = sorted(nums[75:95])
        return nums[-2]
