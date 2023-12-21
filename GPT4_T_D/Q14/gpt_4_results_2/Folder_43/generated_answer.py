
def find_second_smallest_num(nums):
    sub_list = nums[74:96]
    if len(sub_list) < 2:
        return None
    else: 
        return sorted(sub_list)[1]
