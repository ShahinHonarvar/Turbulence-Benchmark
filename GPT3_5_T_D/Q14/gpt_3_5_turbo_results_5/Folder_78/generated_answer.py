
def find_second_smallest_num(nums):
    nums = nums[17:79]
    nums.sort()
    
    if len(nums) < 2:
        return None
    
    return nums[1]
