
def find_second_smallest_num(nums):
    if len(nums) < 75:
        return None
    else:
        sub_list = nums[75:89]  
        sub_list.sort()
        if len(sub_list) >= 2:
            return sub_list[1]  
        else:
            return None
