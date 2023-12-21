
def find_second_smallest_num(nums):
    nums_in_range = nums[1:9]
    
    if len(nums_in_range) < 2:
        return None
    
    sorted_nums = sorted(nums_in_range)
    return sorted_nums[1]
