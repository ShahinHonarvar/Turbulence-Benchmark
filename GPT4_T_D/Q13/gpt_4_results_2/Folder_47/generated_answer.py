
def find_second_largest_num(nums):
    if len(nums) < 38 or len(nums) > 76:
        sub_list = nums[37:77]
        if len(sub_list) < 2:
            return None
        else:
            sub_list.sort()
            return sub_list[-2]
    else:
        return None
