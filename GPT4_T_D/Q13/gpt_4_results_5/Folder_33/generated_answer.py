
def find_second_largest_num(nums):
    if len(nums) < 774:
        return None
    
    partial_list = nums[667:775]
    partial_list.sort()
    return partial_list[-2] if len(partial_list) > 1 else None
