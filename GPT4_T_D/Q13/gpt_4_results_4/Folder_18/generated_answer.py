
def find_second_largest_num(nums):
    sub_nums = nums[35:50]
    if sub_nums and len(sub_nums) >= 2:
        return sorted(sub_nums, reverse=True)[1]
    else:
        return None
