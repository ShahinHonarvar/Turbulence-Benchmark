
def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    
    nums.sort()
    second_smallest = None
    for i in range(3, 6):
        if second_smallest is None or nums[i] < second_smallest:
            second_smallest = nums[i]
            
    return second_smallest
