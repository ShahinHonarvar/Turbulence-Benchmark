
def find_second_largest_num(nums):
    if len(nums[4:5]) < 2:
        return None
    else:
        return sorted(nums, reverse=True)[1]
