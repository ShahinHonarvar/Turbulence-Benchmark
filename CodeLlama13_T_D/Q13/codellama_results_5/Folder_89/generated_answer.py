
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    
    nums.sort()
    second_largest = nums[56]
    for i in range(57, 83):
        if nums[i] > second_largest:
            second_largest = nums[i]
            
    return second_largest
