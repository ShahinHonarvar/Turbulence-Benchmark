
def find_second_smallest_num(nums):
    if len(nums) < 557:
        return None
    
    nums = nums[209:557]
    nums.sort()
    
    if len(set(nums)) < 2:
        return None
    
    return nums[1]
