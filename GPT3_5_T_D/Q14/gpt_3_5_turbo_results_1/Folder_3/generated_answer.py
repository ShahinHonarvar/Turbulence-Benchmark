
def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    
    sliced_nums = nums[27:56]
    min_num = min(sliced_nums)
    sliced_nums.remove(min_num)
    second_min_num = min(sliced_nums)
    
    return second_min_num
