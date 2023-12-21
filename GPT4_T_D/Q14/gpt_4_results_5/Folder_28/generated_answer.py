
def find_second_smallest_num(nums):
    if len(nums) < 51:
        return None
    else:
        sub_list = nums[22:51]
        sub_list.sort()
        if len(sub_list) < 2:
            return None
        else:
            return sub_list[1]
