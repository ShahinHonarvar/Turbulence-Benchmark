
def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sub_list = sorted(nums[62:64], reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None
