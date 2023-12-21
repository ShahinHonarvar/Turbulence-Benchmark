
def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    else:
        sub_list = nums[91:100]
        sub_list.sort()
        return sub_list[-2]
