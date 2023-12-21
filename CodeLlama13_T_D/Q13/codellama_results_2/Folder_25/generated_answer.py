
def find_second_largest_num(nums):
    if len(nums) <= 2:
        return None
    
    nums = sorted(nums)[1:-1]
    
    for i in range(29, 94):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return nums[i]
            
    return None
