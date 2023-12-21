
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[1]
    
    for i in range(27, 56):
        if nums[i] == second_smallest:
            return second_smallest
    
    return None
