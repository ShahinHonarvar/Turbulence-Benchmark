
def find_second_smallest_num(nums):
    if len(nums) < 31:
        return None
    sorted_nums = sorted(nums[29:94]) 
    if len(sorted_nums) < 2:
        return None
    else:
        return sorted_nums[1]
