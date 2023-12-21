
def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    sorted_nums = sorted(nums[70:85])
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[-2]
