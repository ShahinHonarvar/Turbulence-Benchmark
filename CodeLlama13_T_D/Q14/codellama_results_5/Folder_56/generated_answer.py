
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    
    sorted_nums = sorted(nums)
    second_smallest = sorted_nums[1]
    
    for i in range(2, len(sorted_nums)):
        if sorted_nums[i] == second_smallest:
            return None
        
        if sorted_nums[i] < second_smallest:
            second_smallest = sorted_nums[i]
    
    return second_smallest
