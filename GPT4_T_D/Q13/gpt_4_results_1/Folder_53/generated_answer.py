
def find_second_largest_num(nums):
    if len(nums) < 200:
        return None
    else:
        sub_list = nums[100:201]
        sub_list.sort(reverse=True)
        if len(sub_list) > 1:
            return sub_list[1]
        else:
            return None
