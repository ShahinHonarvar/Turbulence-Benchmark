
def find_second_largest_num(nums):
    if 200 <= len(nums) > 30:    
        sliced_list = nums[30:201]
        sliced_list.sort()
        return sliced_list[-2]
    else:
        return None
