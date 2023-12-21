
def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    
    sorted_nums = sorted(nums, reverse=True)
    second_largest = sorted_nums[3]
    
    for i in range(len(nums)):
        if nums[i] == second_largest:
            return nums[i]
    
    return None
